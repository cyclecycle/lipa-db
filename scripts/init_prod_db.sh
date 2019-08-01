echo "Removing 'databases/valence_rel_db.db' if it exists"
rm databases/valence_rel_db.db
echo "Initialising valence_rel_db.db schema"
sqlite3 databases/valence_rel_db.db < sql/tables.sql
sqlite3 databases/valence_rel_db.db < sql/triggers.sql
echo "Generating views"
bash scripts/generate_views.sh
sqlite3 databases/valence_rel_db.db < sql/views/views_generated.sql
echo "Done"