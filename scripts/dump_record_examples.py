import os
import requests
import json
from util import util

config = util.load_config()

tables = [
    'documents',
    'sentences',
    'tokens',
    'patterns',
    'matches',
    'pattern_training_matches',
    'pattern_matches',
    'patterns_view',
    'pattern_matches_view',
    'documents_view',
    'sentences_view',
    'matches_view',
]

url = config['db_rest_url']

target_dir = 'databases/record_examples'

for table in tables:
    query = '{}/?id=1'.format(table)
    query_url = '{0}/{1}'.format(url, query)
    print('Querying:', query_url)
    response = requests.get(query_url)
    try:
        data = response.json()
        json_string = json.dumps(data, ensure_ascii=False, indent=2)
        file_name = '{}.json'.format(table)
        file_path = os.path.join(target_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(json_string)
        print('Wrote to {}'.format(file_path))
    except Exception as e:
        print('Error parsing: \"{}\"'.format(response.text))
