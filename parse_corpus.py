import os
import json
from config import config
from nlp import parse
import util


cwd = util.get_file_directory(__file__)
parser = parse.Parser()


def get_parsed_sentences(text):
    doc = parser.parse(text)
    sentences = []
    for sentence in doc.sents:
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


def spacy_sentence_to_json(sentence, data={}):
    tokens = [spacy_token_to_json(token) for token in sentence]
    data = {
        'text': sentence.text,
        'start': sentence.start_char,
        'length': len(sentence.text),
        'tokens': tokens,
        **data
    }
    return data


def parse_record(record, id_field, content_fields):
    parsed_record = {
        'id': int(record[id_field]),
        'sections': []
    }
    content_sections = [record[field] for field in content_fields]
    for content, field in zip(content_sections, content_fields):
        sentences = get_parsed_sentences(content)
        sentences = [spacy_sentence_to_json(sent, data={'content_field': field}) for sent in sentences]
        parsed_record['sections'].append({
            'text': content,
            'sentences': sentences,
            'content_field': field
        })
    return parsed_record


def parse_corpus(corpus, corpus_fields):
    id_field = corpus_fields['idField']
    content_fields = corpus_fields['contentFields']
    parsed_corpus = [parse_record(record, id_field, content_fields) for record in corpus]
    return parsed_corpus


if __name__ == '__main__':
    corpus_path = os.path.join(cwd, 'mock/corpus.json')
    corpus_schema_path = os.path.join(cwd, 'mock/corpus_fields.json')
    corpus = util.load_json(corpus_path)
    corpus_fields = util.load_json(corpus_schema_path)
    parsed_corpus = parse_corpus(corpus, corpus_fields)
