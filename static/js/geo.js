$(document).ready(function() {
       
      
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success)
        } else {
            console.log("Nope")
        }
      function success(pos) {

            var crd = pos.coords;
            console.log('Your current position is:');
            console.log('Latitude : ' + crd.latitude);
            console.log('Longitude: ' + crd.longitude);
            console.log('More or less ' + crd.accuracy + ' meters.');
        };

});

$('.geo').change(function() {
    if (this.checked) {
        function success(pos) {

            var crd = pos.coords;
            $('.lag').val(crd.latitude)
            $('.log').val(crd.longitude)
            console.log('Your current position is:');
            console.log('Latitude : ' + crd.latitude);
            console.log('Longitude: ' + crd.longitude);
            console.log('More or less ' + crd.accuracy + ' meters.');
        };
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success)
        } else {
            console.log("Nope")
        }
    } else {
        console.log('Not checked')
    }
});