rm databases/record_examples/*.json
source env/bin/activate
echo "Dumping record examples"
PYTHONPATH="." python scripts/dump_record_examples.py