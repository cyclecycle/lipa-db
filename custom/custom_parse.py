import spacy
from custom.valence_annotator import ValenceAnnotator
from sentence_case import sentence_case

SPACY_DISABLE = [
    'ner',
    'entity_ruler',
    'textcat',
    'sentencizer',
    'merge_noun_chunks',
    'merge_entities',
    'merge_subtokens',
]

nlp = spacy.load('en_core_sci_sm', disable=SPACY_DISABLE)
valence_annotator = ValenceAnnotator(nlp)
nlp.add_pipe(valence_annotator, last=True)


def get_parsed_sentences(doc):
    sentences = []
    for sentence in doc.sents:
        sentences.append(sentence)
    return sentences


def spacy_token_to_json(token):
    features = ['tag_', 'dep_', 'lower_']
    feature_dict = {attr: getattr(token, attr) for attr in features}
    feature_dict['_'] = {'valence': token._.valence}
    start_idx_in_sent = token.idx - token.sent.start_char
    data = {
        'text': token.text,
        'start': start_idx_in_sent,
        'length': len(token),
        'features': feature_dict,
        'i': token.i,
    }
    return data


def spacy_sentence_to_json(sentence, data={}):
    doc = sentence.as_doc()
    # Underscore attributes not copied with .as_doc()
    # So copy them over:
    for token_a, token_b in zip(sentence, doc):
        token_b._.valence = token_a._.valence
    tokens = [spacy_token_to_json(token) for token in doc]
    data = {
        'text': sentence.text,
        'start': sentence.start_char,
        'length': len(sentence.text),
        'tokens': tokens,
        'spacy_doc': doc.to_bytes(),
        **data,
    }
    return data


def parse_record(record, id_field, content_fields):
    parsed_record = {'source_document_id': int(record[id_field]), 'sections': []}
    content_sections = [record[field] for field in content_fields]
    for content, field in zip(content_sections, content_fields):
        if field == 'TI':
            doc = nlp.make_doc(content)
            doc = sentence_case(doc, nlp)
        else:
            doc = nlp(content)
        preprocessed_content = doc.text
        sentences = get_parsed_sentences(doc)
        sentences = [
            spacy_sentence_to_json(sent, data={'section': field}) for sent in sentences
        ]
        parsed_record['sections'].append(
            {'text': preprocessed_content, 'sentences': sentences, 'name': field}
        )
    return parsed_record
