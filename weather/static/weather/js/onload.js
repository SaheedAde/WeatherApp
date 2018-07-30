/**
 * Created by Saheed on 30/07/2018.
 */


function myFunction() {
    if (confirm("Permission to read Your Location?")){
        function ipLookUp() {
            $.ajax('http://ip-api.com/json')
            .then(
                function success(response) {
                    var city = response.city;
                    console.log('User\'s City Data is ', city);
                    $(".input").val(city);
                    $("form:first").submit();
                },
                function fail(data, status) {
                    console.log('Request failed. Returned status of', status);
                }
        );
    }
    ipLookUp()
    }else{}
};
window.onload=myFunction;