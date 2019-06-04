rm databases/record_examples/*.json
source env/bin/activate
PYTHONPATH="." python scripts/dump_record_examples.py