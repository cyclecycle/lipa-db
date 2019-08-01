echo "Removing 'databases/test.db' if it exists"
rm databases/test.db
echo "Initialising test.db schema"
sqlite3 databases/test.db < sql/tables.sql
sqlite3 databases/test.db < sql/triggers.sql
echo "Generating views"
bash scripts/generate_views.sh
sqlite3 databases/test.db < sql/views/views_generated.sql
echo "Inserting mock data"
bash scripts/insert_data.sh
bash scripts/dump_record_examples.sh
echo "Done"