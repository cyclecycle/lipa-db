import os
import json


def get_db_path(config):
    mode = config['mode']
    db_path = config['db_paths'][mode]
    return db_path


def get_file_directory(file):
    return os.path.abspath(os.path.dirname(os.path.realpath(file)))


def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def json_string(s):
    return json.dumps(s, ensure_ascii=False)