
# Booleans and Conditionals

## Booleans

Booleans are true/false values. Boolean literals are `true` and `false`.

## Comparisons

You can compare values using comparison operators.

- `==` equal-to, may coerce types
- `===` equal-to, same type
- `!=` not-equal, may coerce types
- `!==` not-equal, same type
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

## Type Coersion

If the two operands of `==` aren't of the same type, the JavaScript interpreter will try to convert them to the same type so they can be compared. This may result in unexpected behavior. In practice, it's better to use `===` which will only be true if both operands are of the **same type and value**.

```javascript
console.log(5 == '5'); // true
console.log(5 == 5); // true
console.log(5 === '5'); // false
console.log(5 === 5); // true
```


## Conditionals

Conditionals in JavaScript require parantheses and curly-braces.

```javascript
let temperature = 56;
if (x < 60) {
    alert('cold');
} else if (x < 80) {
    alert('warm');
} else {
    alert('hot');
}
```

## Truthy and Falsey


JavaScript lets you pass non-boolean types into conditionals, which may evaluate to true or false, depending on what generally makes sense. All values are 'truthy' except `false`, `0`, `""`, `null`, `undefined`, and `NaN`.

```javascript
let x = 0;
if (x) {
    console.log('true!');
} else {
    console.log('false!'); // this will be called
}
```


## Ternary Operator

There's alse a ternary operator, which will let you perform an if-else in one line.

```javascript
function min(a, b) {
    return (a < b)? a: b;
}
```
