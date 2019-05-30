import os
import json
import parse
from config import config


cwd = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
parser = parse.Parser()


# def is_sentence_an_unbroken_tree(sentence):
#     sentence = sentence.as_doc()
#     trees = list(parse.separate_trees(sentence))
#     n_trees = len(trees)
#     if n_trees == 1:
#         return True
#     return False


def get_parsed_sentences(text):
    doc = parser.parse(text)
    sentences = []
    for sentence in doc.sents:
        # sentence_is_an_unbroken_tree = is_sentence_an_unbroken_tree(sentence)
        sentences.append(sentence)
    return sentences


def spacy_token_to_json(token):
    features = config['spacy_token_features']
    feature_dict = {attr: getattr(token, attr) for attr in features}
    start_idx_in_sent = token.idx - token.sent.start_char
    data = {
        'text': token.text,
        'start': start_idx_in_sent,
        'length': len(token),
        'features': feature_dict
    }
    return data


def spacy_sentence_to_json(sentence):
    tokens = [spacy_token_to_json(token) for token in sentence]
    data = {
        'text': sentence.text,
        'start': sentence.start_char,
        'length': len(sentence.text),
        'tokens': tokens
    }
    return data


def parse_record(record, id_field, content_fields):
    parsed_record = {
        'id': int(record[id_field]),
        'sections': []
    }
    content_sections = [record[field] for field in content_fields]
    for content in content_sections:
        sentences = get_parsed_sentences(content)
        sentences = [spacy_sentence_to_json(sent) for sent in sentences]
        parsed_record['sections'].append({
            'text': content,
            'sentence': sentences
        })
    return parsed_record


def parse_corpus(corpus, corpus_fields):
    id_field = corpus_fields['idField']
    content_fields = corpus_fields['contentFields']
    parsed_corpus = [parse_record(record, id_field, content_fields) for record in corpus]
    return parsed_corpus


def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    corpus_path = os.path.join(cwd, '../mock/corpus.json')
    corpus_schema_path = os.path.join(cwd, '../mock/corpus_fields.json')
    corpus = load_json(corpus_path)
    corpus_fields = load_json(corpus_schema_path)
    parsed_corpus = parse_corpus(corpus, corpus_fields)
