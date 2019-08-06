import os
import json


CONFIG_PATH = 'config.json'


def load_config():
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    return config


def get_db_path(config):
    db_file = os.environ['LIPA_SQLITE_DB_FILE']
    db_path = os.path.join('databases', db_file)
    return db_path


def get_file_directory(file):
    return os.path.abspath(os.path.dirname(os.path.realpath(file)))


def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def json_string(s):
    return json.dumps(s, ensure_ascii=False)
