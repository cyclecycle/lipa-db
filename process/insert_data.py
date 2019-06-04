import os
import sqlite3
from config import config
from util import util

cwd = util.get_file_directory(__file__)
db_path = util.get_db_path(config)


def insert_patterns(patterns):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for pattern in patterns:
            pattern_data = util.json_string(pattern['pattern_data'])
            query = 'insert into patterns (name, pattern_data) values (?, ?)'
            cur.execute(query, (pattern['name'], pattern_data,))


def insert_training_examples(training_examples):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for training_example in training_examples:
            slots = training_example['slots']
            data = util.json_string({'slots': slots})
            query = 'insert into training_examples (data, pos_or_neg, sentence_id) values (?, ?, ?)'
            values = (data, training_example['pos_or_neg'], training_example['sentence_id'],)
            cur.execute(query, values)


if __name__ == '__main__':
    pattern_data_path = os.path.join(cwd, '../mock/patterns.json')
    patterns = util.load_json(pattern_data_path)
    insert_patterns(patterns)

    training_example_data_path = os.path.join(cwd, '../mock/training_examples.json')
    training_examples = util.load_json(training_example_data_path)
    insert_training_examples(training_examples)
