# lipa-db

Database and backend functionality for LIPA.

- SQLite databases for test and prod environments
- Exposes them through a REST interface
- Contains mock data
- Processes for parsing and inserting documents into the DB

## Development

### Python

Install dependencies:

```bash
pip install -r requirements.txt
```

Run any python file from the root directory:

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
node rest.js
```

Tests (ensure REST started):

```
npm run test
```

## Build with

- sqlite-to-rest