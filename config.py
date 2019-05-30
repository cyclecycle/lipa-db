config = {
    'mode': 'test',
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