
# XML + JSON

XML and JSON are two popular ways of formatting data.

[JSON](http://www.json.org/) is very similar to javascript object declarations, but the major difference is that the names are strings, and the values can be numbers, strings, arrays, booleans, null, or objects.

```
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
```

[XML](https://developer.mozilla.org/en-US/docs/XML_Introduction) resembles HTML, it has tags, and attributes, and inner text.

```
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

