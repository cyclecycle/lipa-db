'use strict';


//---------//
// Imports //
//---------//

const Koa = require('koa')
const sqliteToRest = require('sqlite-to-rest');
const cors = require('@koa/cors');


//------//
// Init //
//------//

const dbPath = 'databases/test.db'
  , getSqliteRouter = sqliteToRest.getSqliteRouter
  , PORT = 8086;


//------//
// Main //
//------//

const app = new Koa();

getSqliteRouter({ dbPath })
  .then(router => {
    app.use(router.routes())
      .use(router.allowedMethods())
      .use(cors({origin: '*'}))
      .listen(PORT);

    console.log(`Listening on port: ${PORT}`);
  });
