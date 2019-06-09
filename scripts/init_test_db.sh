source env/bin/activate
echo "Removing 'databases/test.db' if it exists"
rm databases/test.db
echo "Initialising test.db schema"
sqlite3 databases/test.db < sql/tables.sql
# sqlite3 databases/test.db < schema/views.sql
echo "Inserting mock data"
bash scripts/insert_data.sh
echo "Dumping record examples"
bash scripts/dump_record_examples.sh
echo "Done"