# LIPA-DB

Database and backend functionality for LIPA.

- SQLite databases for test and prod environments
- Exposes DBs through REST interface
- Contains mock data
- Processes for parsing and inserting documents into the DB

## Scripts

Run all scripts from root directory.

### Initialise database

- Overwrites existing /databases/test.db
- Uses schemas/schema.sql
- Inserts mock data

```bash
bash init_test_db.sh
```

### Start REST server:

```bash
bash scripts/start_rest.js
```

## Development

### Python

Install dependencies:

```bash
pip install -r requirements.txt
```

Run any python file from the root directory with:

```bash
PYTHONPATH="." python /path/to/file
```

### JS

Install dependencies:

```bash
npm install
```

Tests (ensure REST started first):

```
npm run test
```

## Built with

- sqlite-to-rest