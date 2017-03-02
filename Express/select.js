var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'rollins',
	database:'tarveltparking'
});

connection.connect();

var id = '1';

connection.query('select * from PARKINGLEVEL1 where id = ?', id, function(err,result){
	console.log(result)
})