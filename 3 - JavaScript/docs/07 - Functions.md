

# Functions

Function allow us to isolate sections of code. You can learn more about functions [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Build_your_own_function).


There are multiple ways to use functions in JavaScript. Below we're 'declaring a function'. This is automatically added to the top of a file, so it can be called before it's declared.

```JavaScript
function add(a, b) {
    return a + b;
}
console.log(add(5, 2));
```

You can also assign the function to a variable.

```JavaScript
var add = function(a, b) {
    return a + b;
}; // this is a statement, and needs a semi-colon
console.log(add(5, 2))
```


## Default Arguments

```javascript
function add(a, b=1) {
    return a + b;
}
add(5, 2); // 7
add(5); // 6
```
