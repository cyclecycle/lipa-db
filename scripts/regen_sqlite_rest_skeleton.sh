sudo rm -f scripts/start_rest.js
sudo sqlite-to-rest generate-skeleton --db-path databases/test.db
mv skeleton.js scripts/start_rest.js