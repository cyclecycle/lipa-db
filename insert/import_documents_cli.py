import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(cwd, '..')
sys.path.append(root_dir)


import argparse
from util import util
from parse_corpus import parse_corpus
from insert_corpus import insert_parsed_corpus, db_path


parser = argparse.ArgumentParser(description='Command-line utility to import documents into LIPA.')
parser.add_argument('--corpus', help='Path to corpus of documents in JSON format.', required=True)
parser.add_argument('--id-field', help='The document ID field.', required=True)
parser.add_argument('--content-fields', nargs='*', help='The document fields containing the text content to parse and insert into the database.', required=True)

args = parser.parse_args()

corpus_path = args.corpus
id_field = args.id_field
content_fields = args.content_fields

print('Loading corpus file')
corpus = util.load_json(corpus_path)

print('Parsing and inserting into {}'.format(db_path))
for i, record in enumerate(corpus):
    print(i + 1)
    parsed = parse_corpus([record], id_field, content_fields)
    insert_parsed_corpus(parsed)

print('Done')