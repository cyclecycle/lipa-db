import os
import sqlite3
from config import config
from util import util

cwd = util.get_file_directory(__file__)
db_path = util.get_db_path(config)


def insert_pattern_data(patterns):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for pattern in patterns:
            pattern_data = util.json_string(pattern['pattern_data'])
            query = 'insert into patterns (name, pattern_data) values (?, ?)'
            cur.execute(query, (pattern['name'], pattern_data,))


if __name__ == '__main__':
    pattern_data_path = os.path.join(cwd, '../mock/patterns.json')
    patterns = util.load_json(pattern_data_path)
    insert_pattern_data(patterns)
