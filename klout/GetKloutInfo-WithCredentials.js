var Decimal = require("jsdecimal");
var Klout = require("node_klout");
klout = new Klout("yqahypj7nbspfbf3k56wr27g", "json", "v2");

//Twitter handle
var TSN="harishvc";


klout.getKloutIdentity(TSN, function(error, klout_user) {
     var KID = klout_user.id;
       //console.log("Twitter Handle ", TSN, " maps to KloutID ",KID);
       
       klout.getUserScore(KID, function(error, klout_response) {
       //console.log(klout_response);
       console.log(TSN,"Klout Score (full): ", klout_response.score);
       console.log(TSN,"Klout Score (rounded): ", Decimal.round(Decimal(klout_response.score), 2, Decimal.MidpointRounding.AwayFromZero).toString());
       });

       klout.getUserTopics(KID, function(error, klout_response) {
       //console.log(klout_response);
       if (klout_response.length > 0) {
            var aa = [];
    	    for ( var ii = 0; ii < klout_response.length; ii++) {
                            aa.push(klout_response[ii].displayName);
            }
    	 console.log(TSN,"Topics of interest: ", aa.toString());
       }
      });  //end topics
});
