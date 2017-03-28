var restify = require('restify'),
    mysql = require('mysql');

var server = restify.createServer({
    name: 'TarParking',
});

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'rollins',
    database: 'tarveltparking'
});

connection.connect(function(err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }
});

server.listen(8080);

server.get('/', function (req, res, next) {
    res.send(connection.database);
    return next();
});

