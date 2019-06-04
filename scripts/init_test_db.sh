echo "Removing 'databases/test.db' if it exists"
rm databases/test.db
echo "Initialising test.db with 'schemas/schema.sql'"
sqlite3 databases/test.db < schemas/schema.sql
echo "Inserting mock data"
bash scripts/insert_data.sh
echo "Dumping record examples"
bash scripts/dump_record_examples.sh
echo "Done"