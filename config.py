config = {
    'mode': 'test',
    'db_rest_url': 'http://localhost:8085/',
    'db_paths': {
        'test': 'databases/test.db',
        'prod': 'databases/prod.db'
    },
    'spacy_model': 'en_core_web_sm',
    'spacy_token_features': [
        'tag_',
        'dep_',
        'lower_',
    ]
}
