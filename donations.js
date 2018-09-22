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
  var sql = "CREATE TABLE donations (email VARCHAR(255), electronics INT(11), vehicles INT(11), books INT(11), clothing INT(11), kitchen INT(11), furniture INT(11), cds INT(11), sporting INT(11), toys INT(11), non-perishable INT(11), medical INT(11), PRIMARY KEY (email))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});