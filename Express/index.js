var express = require('express')
var mysql = require('mysql');

var app = express()
 
var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'rollins',
	database:'tarveltparking'
});


connection.connect();

var id = '1';


app.get('/', function(req, res) {

	connection.query('select * from PARKINGLEVEL1 where id = ?', id, function(err,result){
	res.json({notes: result})
	connection.release();
});

});
 
app.listen(3000)

