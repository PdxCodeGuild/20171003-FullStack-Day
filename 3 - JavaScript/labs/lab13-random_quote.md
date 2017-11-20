



# Lab 13: Random Quote


Use the [favqs.com](https://favqs.com/api/) api to show a random quote. To start, use `https://favqs.com/api/qotd` to `GET` a quote, then display it on the page.

Next let's get a random quote by requesting a quote with a random id. We can use `https://favqs.com/api/quotes/<quote_id>` and put a random number in place of quote id. Use a random int in the range 0-1000.

For example `https://favqs.com/api/quotes/4` returns 

```json
{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
```

In order to get authorization for this request, we need to add a request header with the authorization token using [setRequestHeader](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader). I'll give you the API key through slack. You can then put it in this altered version of our http_get function, or do it yourself. **DO NOT CHECK IN CODE CONTAINING THIS KEY.** Also note that it's possible to request a quote that doesn't exist, so we'll have to handle any 404 responses.

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="<api kep here>"')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}
```


## Version 2

Add an `input` field and a `button`, allow users to enter some text and find quotes by using `https://favqs.com/api/quotes/?filter=<text>`. Retrieve the quotes you get in response and show them in a list. Note that if the text has spaces or special characters will have to encode the parameters using [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) which takes a string and returns a new encoded string.

## Version 3 (optional)

Use `/api/typeahead` to show a list of suggestions as the user types.