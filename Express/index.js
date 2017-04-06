var express = require('express');
//var session = require('cookie-session');
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

var app = express();


// JSON testing
app.get('/', function(req, res) {
    res.json({
        "data":"hello world"
       });
 })

// Can't get anything else
.use(function(req, res, next){
    res.setHeader('Content-Type', 'text/plain');
    res.status(404).send('Page Error !');
    })


.listen(8090)