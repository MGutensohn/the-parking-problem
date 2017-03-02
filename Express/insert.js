var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'rollins',
	database:'tarveltparking'
});

connection.connect();

var parking = {
	OCCUPIED : 1,
};

var query = connection.query('insert into PARKINGLEVEL1 set ?', parking, function (err, result){
		if (err) {
			console.error(err);
			return;
		}

		console.error(result);
});







