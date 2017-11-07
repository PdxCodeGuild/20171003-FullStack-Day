
# Fundamentals

## Declaring Variables

There are three ways to declare variables: `var`, `let` and `const`.

`var` and `let` are very similar, the only difference is that `let` more closely follows scope. You should use `let` by default.

```
if (2 < 10) {
    var x = 10;
    let y = 11;
}
console.log(x); // 10
console.log(y); // error

for (var x=0; x<10; ++x) {}
alert(x); // 10

for (let y=0; y<10; ++i) {}
alert(y); // error


```

`const` variables cannot change value, this is advantageous for declaring constants.

```javascript
const pi = 3.1415;
pi += 1 // error
```


## Data Types

```JavaScript
let a = 5; // int
let b = 10.4; // float
let c = "hello!"; // string
let d = true; // boolean
let e = null; // null
let f = undefined; // undefined

let fruits = ["apple", "bananana", "pear"]; // array

let person = {firstName:"John", lastName:"Doe", age:46}; // object
person.age += 1;
person.favorite_fruit = "orange";
```

To convert between types, use `parseInt`, `parseFloat` and `toString`.

```JavaScript
let x = parseInt('4');
let y = parseFloat('4.2');
let z = x.toString();
```


## Comments

Use `//` for line-comments, `/* ... */` for block-comments.

```javascript
// this is a line comment
let x = 10; // this is another line comment
/* this is a block comment
which can span multiple lines*/
```

## The Script Tag

In an HTML page, we can specify blocks of JavaScript code using `<script>` tags. You can put these anywhere, but most often you'll put them in the `<head>` or at the bottom of the `<body>`. You may see a `type="text/javascript"` attribute on script tags. This was necessary in HTML4.01, but not in HTML5.

```html
<html>
    <head>
        <script>
            alert('put your code here');
        </script>
    </head>
    <body>
        ...
        <script>
            alert('or here');
        </script>
    </body>
</html>
```

If you put in the head, you cannot do `document.getElementById`, `document.querySelector`, etc, on the elements in the body, because the JavaScript would be executed before the body is loaded. You have to either wrap it in a `window.onload = function () {...}` or put it at the bottom of the body.

A script tag may also reference an external file containing JavaScript, denoted with a `.js` suffix.

```html
<script src="myscript.js"></script>
```

JavaScript can also be written in-line.

```html
<button onclick="alert('Hello World!');">click me</button>
```


## Input


An easy way to get input from a user is `prompt`, a function which takes the text to display as a parameter and returns whatever the user entered.

```javascript
let name = prompt("Please enter your name");
alert("Hello " + name + "! How are you today?");
```

## Output

Below are three simple ways of getting output to the user.

`alert` shows the given sting to the use in a pop-up

```javascript
alert('Hello World!');
```


`console.log` will print an object in the developer console (F12), giving much more control than `alert`.


```javascript
console.log("Hello World!");
```

`document.write(s)` will replace all existing HTML on the page with whatever you give it (which can be a string containing HTML)

```javascript
document.write('Hello World!');
```

