

# Numbers and Arithmetic

Unlike other languages, JavaScript doesn't have a special 'int' type, only a 64-bit float type called `number`. There are 5 arithmetic operators, addition, subtraction, multiplication, division, and modulus. The modulus of `a` and `b` (`a%b`) is the remainder of `a/b`. You can read more about arithmetic [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators)

```javascript
5 + 1 // 6
5 - 1 // 4
2 * 3 // 6
2 / 3 // 1.5
2 % 3 // 2
```

There are also operations which edit the original variable.

```javascript
let a = 1;
a += 3;  // a = a + 3
a -= 2;  // a = a - 2
a *= 5;  // a = a * 5
a /= 10; // a = a / 10
a++;     // a = a + 1, a += 1
++a;     // a = a + 1, a += 1
a--;     // a = a - 1, a -= 1
--a;     // a = a - 1, a -= 1
```

## Math

The built-in object `Math` has additional operations that can be performed on numbers. You can read more about `Math` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math).

```JavaScript
Math.abs(-4) // 4
Math.sqrt(16) // 4.0
Math.min(5, 6) // 5
Math.max(5, 6) // 6
Math.floor(4.5) // 4
Math.ceil(4.5) // 5
Math.round(4.5) // 5
Math.random() // between 0 and 1, but not including 1
Math.pow(5, 2) // 25
Math.PI // 3.1415...
Math.sin(Math.PI/2) // 1.0
Math.cos(Math.PI/2) // 0.0
```