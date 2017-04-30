/**
 * Server.JS is the creation of the backend of the parking problem.
 * It connects with Twilio and MySQL to gather data that the pi insert into
 * the table and sends it to respective routes that a customer may want. The twilio
 * is showing it is possible to send data via text. The extra step for twilio is to start ngrok
 * to get a global address and sending it to people. Everything else is local. Google Cloud happen
 * to not connect properly due to issues that couldn't be figured out in time. **/


// [START app]
'use strict';

// [START setup]
const express = require('express');
const mysql = require('mysql');
const crypto = require('crypto');
const cors= require('cors');
const http = require('http');
const twilio = require('twilio');

const app = express();
app.enable('trust proxy');
// [END setup]

app.use(cors({origin: 'http://localhost:8101'}));

// [START connect]
var config = {
  host: 'localhost',
  port:'3306',
  user: 'root',
  password: 'rollins',
  database: 'tarveltparking'
};

// Connect to the database
const connection = mysql.createConnection(config);
// [END connect]

// creates query to pull in available spots
const SQL_STRING = 'SELECT COUNT(*) as counts FROM floor_one WHERE spot_avail = 0;';

// method to run query with error statement
function getCount (callback) {
  connection.query(SQL_STRING, (err, results) => {
    if (err) {
      callback(err);
      return;
    }
    
    callback(null, results.map((data) => ` ${data.counts}`));
  });
}

/*** This is the real Route Information ***/
app.get('/', (req, res, next) => {

    // Query the count from the database.
    getCount((err, data) => {
      if (err) {
        next(err);
        return;
      }
// this sends the data to the root route
      res
        .status(200)
        .set('Content-Type', 'text/plain')
        .send(`${data}`);
    });
});

// This is the twilio route where the twilio app sends gets to send the thata.
app.post('/sms', (req, res) => {
  const twilio = require('twilio');
  const twiml = new twilio.TwimlResponse();
  getCount((err, data) => {
      if (err) {
        next(err);
        return;
      }
        
      twiml.message('There are ${data} spots available');
      res.writeHead(200, {'Content-Type': 'text/xml'});
      res.end(twiml.toString());
    });
  
});

// when it runs it is going to be on this port so ngrok you just need the port number.
const PORT = process.env.PORT || 1337;
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
  console.log('Press Ctrl+C to quit.');
});

module.exports = app;