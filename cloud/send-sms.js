// Twilio Credentials 
var accountSid = 'ACfd75a723a530e11457b33307b1e0fcef'; 
var authToken = 'ad45c6b6055126c8ef1edb2072e2fe5d'; 
 
//require the Twilio module and create a REST client 
var client = require('twilio')(accountSid, authToken); 
 
client.messages.create({ 
    to: "+14074846710", 
    from: "+13212340514", 
    body: "This is the ship that made the Kessel Run in fourteen parsecs?", 
}, function(err, message) { 
    console.log(message.sid); 
});