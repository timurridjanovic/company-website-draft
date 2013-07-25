var address = '1404 rue beliveau, Sherbrooke, Quebec';

var map = new google.maps.Map(document.getElementById('map'), { 
	mapTypeId: google.maps.MapTypeId.ROAD,
       	zoom: 12
});

var geocoder = new google.maps.Geocoder();


geocoder.geocode({
	'address': address
	}, 
   
	function(results, status) {
		if(status == google.maps.GeocoderStatus.OK) {
         		new google.maps.Marker({
            			position: results[0].geometry.location,
            			map: map
         		});
         		map.setCenter(results[0].geometry.location);
      		}
      		
		else {
         		// Google couldn't geocode this request. Handle appropriately.
      		}
  	});
