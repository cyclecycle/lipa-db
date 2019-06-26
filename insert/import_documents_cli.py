import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(cwd, '..')
sys.path.append(root_dir)


import argparse
from util import util
from parse_corpus import parse_corpus
from insert_corpus import insert_parsed_corpus


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

print('Parsing corpus')
parsed_corpus = parse_corpus(corpus, id_field, content_fields)

print('Inserting documents')
insert_parsed_corpus(parsed_corpus)

print('Done')