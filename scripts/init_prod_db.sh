echo "Removing 'databases/$LIPA_SQLITE_DB_FILE' if it exists"
rm databases/$LIPA_SQLITE_DB_FILE
echo "Initialising $LIPA_SQLITE_DB_FILE schema"
sqlite3 databases/$LIPA_SQLITE_DB_FILE < sql/tables.sql
sqlite3 databases/$LIPA_SQLITE_DB_FILE < sql/triggers.sql
echo "Generating views"
bash scripts/generate_views.sh
sqlite3 databases/$LIPA_SQLITE_DB_FILE < sql/views/views_generated.sql
echo "Done"