$(function(){
	
		
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

   var time=0;
   var title="";
   var redirect="";
   time = getParameterByName('time');
   title = getParameterByName('title');
   redirect = getParameterByName('redirect');
   
   //Debug
   //console.log("parameters 12345....");
   //console.log("time -->" ,  time);   
   //console.log("title --->", title);   
   //console.log("redirect --->",redirect);   
   $('#title').html(title);


	var note = $('#note'),
		ts = new Date(2012, 0, 1),
		newYear = true;
	
	if((new Date()) > ts){
		// The new year is here! Count towards something else.
		// Notice the *1000 at the end - time must be in milliseconds
                //1 days from now
		//ts = (new Date()).getTime() + 1*24*60*60*1000;
		//25 seconds from now
		ts = (new Date()).getTime() + time*60*1000;
		newYear = false;
	}



	$('#countdown').countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){
			
			var message = "starting in ";
			
			if (days != 0) { message += days + " day" + ( days==1 ? '':'s' ) + ", ";}
			if (hours!= 0) {message += hours + " hour" + ( hours==1 ? '':'s' ) + ", "; }
			if (minutes!= 0){message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";}
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + " <br />";
			
			//if(newYear){
			//	message += "left until the new year!";
			//}
			//else {
			//	message += "left to 10 days from now!";
			//}
			
			note.html(message);
			//console.log(message);
                   

                       if( (days==0 && hours==0 && minutes==0 && seconds ==0)) {
                           //console.log("redirecting ...");
                           location.href=redirect;
                         }
		}
	});
	
});
