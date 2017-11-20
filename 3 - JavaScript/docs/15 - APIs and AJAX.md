
# APIs and AJAX

## API

API stands for "application programming interface", it's a standardized way to send and receive data from a web service via HTTP requests (GET, POST, PUT, DELETE). For example, try executing this url in your browser `http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en`. This is an api for random inspiration quotes. Note the query parameters, which specify a key, format, and language. When you enter it in your browser, you execute an HTTP GET request. You can do the same thing from JavaScript, then process the result and control how it's displayed to the user. Websites are for people, APIs are for programs.

There are many free and open APIs available on the internet that can provide many different forms of data. You can find some public APIs [here](https://github.com/toddmotto/public-apis) and [here](https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation).



### HTTP Methods

HTTP requests include a **method**, which indicates what the intention of the request is. These methods are conventional. You could use `GET` to delete an entry in the database, but you shouldn't. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods). The most common HTTP methods parallel the CRUD operations we discussed in Python.

| Method | Equivalent |
| ---    | ---        |
| POST   | Create     |
| GET    | Retrieve   |
| PUT    | Update     |
| DELETE | DELETE     |


### HTTP Status Codes

The response to an HTTP request will have a **status code** which indicates whether the request was successful or not, and what the error was. You can find a more thorough list of status codes [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

| Code | Description  |
| ---  | ---          |
| 1XX  | information  |
| 2XX  | success      |
| 3XX  | redirection  |
| 4XX  | client error |
| 5XX  | server error |


## AJAX

AJAX stands for "asynchronous javascript and XML", and allows you to execute HTTP requests from JavaScript. You can read more about AJAX [here](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started), [here](https://developer.mozilla.org/en-US/docs/AJAX) and [here](https://www.w3schools.com/xml/ajax_intro.asp).


Here's how to execute an AJAX request in native JavaScript. You can read more about XMLHttpRequest [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest). Remember status 200 means 'success'.

```javascript
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
    }
};
xhttp.open("GET", 'https://api.iify.org/?format=json');
xhttp.send();
```

The possible values for `readyState` are shown below, you can find more info [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)
- 0 UNSENT: the request has not yet been sent
- 1 OPENED: the connection has been opened
- 2 HEADERS_RECEIVED: the response headers have been received
- 3 LOADING: the response body is loading
- 4 DONE: the request has been completed

Here I've wrapped an AJAX request in a function to make it easier to use:

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

http_get("https://api.ipify.org/?format=json", function(data) {
    console.log(data);
});
```

It's a little more succinct in jQuery:

```javascript
$.ajax({
    method: "GET", // specify the HTTP Verb
    url: 'https://api.iify.org/?format=json' // specify the URL
}).done(function(data) {
    console.log(data); // log the data we get in response
}).fail(function() {
    alert("error"); // indicate that an error has occurred
});
```
If you receive the response "No 'Access-Control-Allow-Origin' header is present on the requested resource", it's because the remote server you're sending to the request from has security controls in place that prevent access from a client. You can read more  [here](https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe).



## JSON + XML

JSON and XML are two popular ways of formatting data. Most APIs either return information in JSON or XML.

[JSON](http://www.json.org/) is very similar to javascript object declarations, but the major difference is that the names are strings, and the values can only be numbers, strings, arrays, booleans, null, or objects.

```json
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
```

[XML](https://developer.mozilla.org/en-US/docs/XML_Introduction) resembles HTML, it has tags, and attributes, and inner text.

```xml
<employees>
    <employee>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
    </employee>
    <employee>
        <firstName>Anna</firstName>
        <lastName>Smith</lastName>
    </employee>
    <employee>
        <firstName>Peter</firstName>
        <lastName>Jones</lastName>
    </employee>
</employees>
```

