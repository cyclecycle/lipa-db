rm databases/record_examples/*.json
echo "Dumping record examples"
PYTHONPATH="." python scripts/dump_record_examples.py