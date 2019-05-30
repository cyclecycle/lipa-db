import os
import sqlite3
from config import config
import util
from parse_corpus import parse_corpus

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
                text = sentence['text']
                sentence = util.json_string(sentence)
                insert_query = 'insert into sentences(document_id, sentence_text, data) values (?, ?, ?)'
                cur.execute(insert_query, (document_id, text, sentence,))


if __name__ == '__main__':
    corpus_path = os.path.join(cwd, 'mock/corpus.json')
    corpus_fields_path = os.path.join(cwd, 'mock/corpus_fields.json')
    corpus = util.load_json(corpus_path)
    corpus_fields = util.load_json(corpus_fields_path)
    parsed_corpus = parse_corpus(corpus, corpus_fields)
    insert_parsed_corpus(parsed_corpus)
