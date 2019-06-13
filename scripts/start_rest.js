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

getSqliteRouter({ dbPath })
  .then(router => {
    app.use(router.routes())
      .use(router.allowedMethods())
      .use(cors({origin: 'http://localhost:8080', 'allowHeaders': 'range', 'keepHeadersOnError': true}))
      .listen(PORT);

    console.log(`Listening on port: ${PORT}`);
  });
