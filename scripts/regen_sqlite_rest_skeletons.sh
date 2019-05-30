sudo rm -f skeleton.js
sudo sqlite-to-rest generate-skeleton --db-path databases/test.db
node skeleton.js