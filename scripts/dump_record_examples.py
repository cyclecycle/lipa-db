import os
import requests
import json
from config import config

tables = [
    'documents',
    'sentences',
    'tokens',
    'patterns',
]

url = config['db_rest_url']

target_dir = 'databases/record_examples'

for table in tables:
    query_url = '{0}{1}'.format(url, table)
    query_params = {'id': '1'}
    response = requests.get(query_url, query_params)
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
