# LIPA-DB

Database and backend functionality for LIPA.

- SQLite databases for test and prod environments
- Exposes DBs through REST interface
- Contains mock data
- Processes for parsing and inserting documents into the DB

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

Activate the REST interface:

```bash
node scripts/start_rest.js
```

Tests (ensure REST started first):

```
npm run test
```

## Built with

- sqlite-to-rest