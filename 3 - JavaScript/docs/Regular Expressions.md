# Regular Expressions

Regular expressions (regex) are patterns used to match character combinations in strings. In JavaScript, you can either call methods on a regular expression object or you can use regex in methods called on strings. You can read more about regular expressions [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) and [here](https://www.sitepoint.com/expressions-javascript/). You may also find these useful: [regexlib.com](http://www.regexlib.com/) and [regex101.com](https://regex101.com/).



There are two ways of defining regex patterns. One uses slashes, the other uses `RegExp` class.

```javascript
var re_a = /ab+c/;
var re_b = new RegExp('ab+c');
```

Once you have a pattern, you can use it to validate strings, text strings, extract values from strings, etc.

```javascript
var re = /ab+c/; // matches abc, abbc, abbbc abbbbc, etc
re.test('abc'); // true
re.test('abbbc'); // true
```

## Special Characters

There are several special characters you can use to denote different things in regex-land. Note that to match something like `.` or `*`, you need to "escape" the character using a backslash: `\.` or `\*`.

- `.` match any valid character
- `\d` match any digit character (0-9)
- `\s` match any whitespace character (space, \t, or \n)
- `\w` match any word character (A-Z, a-z, 0-9, and _)
- `*` match 0 or more instances of the preceding character
- `+` match 1 or more instances of the preceding character
- `?` match 0 or 1 instance of the preceding character
- `{a,b}` match between a and b of the preceding character


## Matching Ranges

You can specify ranges of characters to be matched. Note that because dashes are used to create ranges, to match a dash character, you need to escape it with a backslash `\-`.

- `[0-9]` match any of the digits 0 through 9
- `[A-Z]` match any uppercase letter from A to Z
- `[a-z0-9]` match any lowercase letter from a to z or any digit 0 to 9


## Capturing Matches

You can "capture" matches or parts of matching patterns using parentheses.

```javascript
var matches = 'jane@doe.com'.match(/.*@(.*\..*)/);
console.log('The hostname is ' + matches[1]);
```