import os
import sqlite3
from util import util
import pickle

config = util.load_config()
cwd = util.get_file_directory(__file__)
db_path = util.get_db_path(config)


def insert_matches(matches):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for match in matches:
            query = 'insert into matches (sentence_id, data) values (?, ?)'
            values = (
                match['sentence_id'],
                util.json_string(match['data']),
            )
            cur.execute(query, values)


def insert_pattern_matches(matches):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for match in matches:
            query = 'insert into pattern_matches (pattern_id, match_id) values (?, ?)'
            values = (
                match['pattern_id'],
                match['match_id'],
            )
            cur.execute(query, values)


def insert_patterns(patterns):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for pattern in patterns:
            query = 'insert into patterns (name, role_pattern_instance) values (?, ?)'
            values = (
                pattern['name'],
                sqlite3.Binary(pickle.dumps(pattern['role_pattern_instance'])),
            )
            cur.execute(query, values)


def insert_training_matches(training_matches):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for training_match in training_matches:
            query = 'insert into pattern_training_matches (match_id, pattern_id, pos_or_neg) values (?, ?, ?)'
            values = (
                training_match['match_id'],
                training_match['pattern_id'],
                training_match['pos_or_neg'],
            )
            cur.execute(query, values)


if __name__ == '__main__':
    matches_data_path = os.path.join(cwd, '../mock/matches.json')
    matches = util.load_json(matches_data_path)
    insert_matches(matches)

    pattern_data_path = os.path.join(cwd, '../mock/patterns.json')
    patterns = util.load_json(pattern_data_path)
    insert_patterns(patterns)

    training_matches = os.path.join(cwd, '../mock/pattern_training_matches.json')
    training_matches = util.load_json(training_matches)
    insert_training_matches(training_matches)

    pattern_matches_path = os.path.join(cwd, '../mock/pattern_matches.json')
    pattern_matches = util.load_json(pattern_matches_path)
    insert_pattern_matches(pattern_matches)
