var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "goodwillDB"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE user (firstName VARCHAR(255), lastName VARCHAR(255), email VARCHAR(255), phone INT(10), type VARCHAR(10), address VARCHAR(255), reason VARCHAR(255), donationCount INT(11), boughtCount INT(11), PRIMARY KEY (email))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});