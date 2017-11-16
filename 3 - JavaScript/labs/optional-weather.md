

# Lab 10: Current Weather


Let's write an app that displays the current weather.

1) Get the user's IP address. This can be done by sending a request to the following URL: https://api.ipify.org/?format=json

2) Using the IP address, get the user's latitude and longitude. This can be done with the `ipapi.co` API. The following URL gets the location for IP address '8.8.8.8'. You'll have to substitute the IP address from the last step. https://ipapi.co/8.8.8.8/json/ 

3) Using the latitude and longitude, get the user's current weather. The following URL gets the current weather for latitude 74.39626435526534 and longitude -13.386707708041683. You'll have to substitute the results from the last step. http://api.openweathermap.org/data/2.5/weather?lat=74.39626435526534&lon=-13.386707708041683&appid=b03cb314cd65e6faa00dc416bd075c78

4) Once you have the JSON object containing the current weather, pull the revelant data out and display it to the user.


Look in the docs folder at 'APIs and AJAX.md'. I've written a helper function which takes a URL and a success function, executes an HTTP GET on the URL, parses the result, and passes it to the 'success' function.

```JavaScript
function http_get(url, success) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            var data = JSON.parse(this.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}


var ip_url = 'https://api.ipify.org/?format=json';
http_get(ip_url, function(data) {
    console.log(data);
});

```

## Advanced 1: Weather Icons

Download this icon set for Open Weather Map: https://websygen.github.io/owfont/#chris-march-2017. You'll have to download the zip, extract its contents to the same folder as your HTML file, and put a link in your head to the CSS file inside. Then when you get the data from the Open Weather Map API, build some HTML to show an icon using the weather's ID. There are example usages at the bottom of the page.

## Advanced 2: Moon Phase

Using the following API, you can get the . You'll have to format the date, latitude, and longitude accordingly. Note that for latitude and longitude, the numbers have N/S/E/W and none of them are negative. You'll have to to transform the latitutde and longitude from the previous step into this format.

http://api.usno.navy.mil/rstt/oneday?date=12/1/2016&coords=41.89N,12.48E

Once you've received this data, look at `fracillum` and `curphase`. This'll tell you what percentage of the moon is visible and the current phase of the moon. You can then use the plugin below to draw what the moon looks like.

https://codebox.net/pages/html-moon-planet-phases
