'use strict';


//---------//
// Imports //
//---------//

const Koa = require('koa')
  , sqliteToRest = require('sqlite-to-rest')
  , cors = require('@koa/cors');


//------//
// Init //
//------//

const dbPath = 'databases/test.db'
  , getSqliteRouter = sqliteToRest.getSqliteRouter
  , PORT = 8085;


//------//
// Main //
//------//

const app = new Koa();

const corsOptions = {
  origin: '*',
  keepHeadersOnError: true,
}

const onConnectionCallback = (db) => {
  db.run('PRAGMA foreign_keys=ON')
}

getSqliteRouter({ dbPath, onConnectionCallback })
  .then(router => {
    app.use(router.routes())
      .use(router.allowedMethods())
      .use(cors(corsOptions))
      .listen(PORT);

    console.log(`Listening on port: ${PORT}`);
  });
