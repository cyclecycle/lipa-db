import os
import sqlite3
from util import util
from parse_corpus import parse_corpus

config = util.load_config()
cwd = util.get_file_directory(__file__)
db_path = util.get_db_path(config)


def insert_parsed_corpus(parsed_corpus):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for record in parsed_corpus:
            for section in record['sections']:
                sentences = section.pop('sentences')
            document = util.json_string(record)
            cur.execute('insert into documents(data) values (?)', (document,))
            document_id = cur.lastrowid
            for sentence in sentences:
                tokens = sentence.pop('tokens')
                text = sentence['text']
                spacy_doc = sentence.pop('spacy_doc')
                spacy_vocab = sentence.pop('spacy_vocab')
                data = util.json_string(sentence)
                query = 'insert into sentences(document_id, text, data) values (?, ?, ?)'
                values = (document_id, text, data,)
                cur.execute(query, values)
                sentence_id = cur.lastrowid
                query = 'insert into sentence_linguistic_data(sentence_id, spacy_doc, spacy_vocab) values (?, ?, ?)'
                values = (sentence_id, sqlite3.Binary(spacy_doc), sqlite3.Binary(spacy_vocab),)
                cur.execute(query, values)
                for token in tokens:
                    token_offset = token.pop('i')
                    token = util.json_string(token)
                    query = 'insert into tokens(sentence_id, token_offset, data) values (?, ?, ?)'
                    cur.execute(query, (sentence_id, token_offset, token,))


if __name__ == '__main__':
    corpus_path = os.path.join(cwd, '../mock/corpus.json')
    corpus_fields_path = os.path.join(cwd, '../mock/corpus_fields.json')
    corpus = util.load_json(corpus_path)
    corpus_fields = util.load_json(corpus_fields_path)
    parsed_corpus = parse_corpus(corpus, corpus_fields)
    insert_parsed_corpus(parsed_corpus)
