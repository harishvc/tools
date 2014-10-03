var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;
var async = require('async');

mystart();

//http://stackoverflow.com/questions/25659134/insert-error-using-node-js-async-series
function mystart () {
var connectURL = "mongodb://harishvc:gitmongo2306@kahana.mongohq.com:10095/github";
var mycollection= "pushevent";
var count = 5;
var db;
var col;

async.series([
  // Connect to DB
  function(callback) {
	  MongoClient.connect(connectURL,function(error, db2) {
		  if (error) {console.log("db connect error");callback(error,"db connect error"); return;} 
		  db = db2;
		  callback(null,"connect success");
	  });
  },
  function(callback) {
	  col = db.collection(mycollection);
      callback(null,"collection success");
  },
  function(callback) {
	  console.log ("insert begin ...");		          
	  var i = 1;
	  async.whilst(
	    function() { return i <= count },
	    function(callback) {
	        col.insert({ c: i },function(error,result) {
	            if (error) {
	                console.log("insert error:" + i);
	                callback(error);
	                return;
	            }
	            console.log ("inserted ..." + i);
	            i++;
	            callback(error);
	        });
	    },
	    function(error) {
	      callback(error,"insert sucess")
	    }
	  );
  },
  function (callback){
	  console.log ("close db");db.close();
	  callback(null,"connection closed");
  }
 ], function(error, results) {
		if (error) { console.log("error"); }
			console.log(results);
	});
}
