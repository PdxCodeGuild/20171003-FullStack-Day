

# Lab 10: Current Weather

Let's write an app that displays the current weather. Check out the [openweathermap api](https://openweathermap.org/current). Try out a query like

`http://api.openweathermap.org/data/2.5/weather?q=london&appid=<your_api_key>`

In response, you'll get an object containing various information. Choose whatever you'd like to display.

- latitude & longitude
- temperature
- pressure
- humidity


## Advanced 1

Using the 'icon' attribute inside the 'weather' part of the response, you can get the url to an icon. You can then just set the `src` of an `img` tag. You can read more about the icons [here](http://openweathermap.org/weather-conditions).

For example, the request `http://api.openweathermap.org/data/2.5/weather?q=London` will get the response

```json
{
    ...
    "weather": [
        {
            "id": 500,
            "main": "Rain",
            "description": "light rain",
            "icon": "10n" // <-------------
        }
    ],
    ...
}
```

We can access the img with the url `http://openweathermap.org/img/w/10n.png`




## Advanced 2

Instead of letting the user specify the location, let's look up their approximate location using their IP address.

1) Get the user's IP address. This can be done by sending a request to the following URL: https://api.ipify.org/?format=json

2) Using the IP address, get the user's latitude and longitude. This can be done with the `ipapi.co` API. The following URL gets the location for IP address '8.8.8.8'. You'll have to substitute the IP address from the last step. https://ipapi.co/8.8.8.8/json/ 

3) Using the latitude and longitude, get the user's current weather. The following URL gets the current weather for latitude 74.39626435526534 and longitude -13.386707708041683. You'll have to substitute the results from the last step. `http://api.openweathermap.org/data/2.5/weather?lat=74.39626435526534&lon=-13.386707708041683&appid=<api_key>`

4) Once you have the JSON object containing the current weather, pull the revelant data out and display it to the user.


## Advanced 3

Download this icon set for Open Weather Map: https://websygen.github.io/owfont/#chris-march-2017. You'll have to download the zip, extract its contents to the same folder as your HTML file, and put a link in your head to the CSS file inside. Then when you get the data from the Open Weather Map API, build some HTML to show an icon using the weather's ID. There are example usages at the bottom of the page.

