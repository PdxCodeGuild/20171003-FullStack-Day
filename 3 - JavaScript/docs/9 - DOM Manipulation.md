
# DOM Manipulation

JavaScript provides many functions to manipulate the DOM. You can find more info [here](https://www.w3schools.com/js/js_htmldom_document.asp).

## Accessing Elements

You can access the elements of the DOM from JavaScript using several functions. You can find more info on these functions [here](https://javascript.info/searching-elements-dom).


| function | description |
| ---      | ---         |
| `document.getElementById(id)` | get an element with the given id |
| `document.getElementsByTagName(tag)` | get all elements of the given tag |
| `document.getElementsByName(name)` | get all elements with the given name |
| `document.querySelector(selector)` | get an element that matches the given CSS selector |
| `document.querySelectorAll(pattern)` | get all elements that match the given CSS selector |

The following code demonstrates how each of these are used:

```html
<div id="mydiv" name="adiv" class="myclass"></div>
<div id="thisdiv" class="myclass"></div>
<div id="thatdiv" name="adiv"></div>

<script>
    let a = document.getElementById('mydiv');
    let bs = document.getElementsByTagName('div');
    console.log(bs.length); // 3
    let cs = document.getElementsByName('adiv');
    console.log(cs.length); // 2
    let d = document.quertSelector('#mydiv');
    let es = document.querySelectorAll('.myclass');
    console.log(es.length); // 2
</script>
```


## Setting innerText and innerHTML

You can set the value 'inside' a tag `<div>this</div>` using `innerText` and `innerHTML`. As you might guess, `innerText` is for text, `innerHTML` is for a string containing HTML.

```html
<div id="div1"></div>
<div id="div2"></div>
<script>
    let div1 = document.querySelector('#div1');
    div1.innerText = "Hello World!";
    
    let div2 = document.querySelector('#div2');
    div2.innerHTML = "<p><b>Hello World!</b></p>";
</script>
```
This renders the following:

```html
<div id="div1">Hello World!</div>
<div id="div2"><p><b>Hello World!</b></p></div>
```

## Editing Attributes and Style

You can assign attributes to elements just as you'd assign attributes to objects.

```html
<div id="demo_div"></div>
<script>
    let demo_div = document.querySelector('#demo_div');
    demo_div.innerHTML = "Hello World!";
    demo_div.style.fontSize = '24px';
    demo_div.name = "demo_div";
</script>
```

This renders the following:

```html
<div id="demo_div" style="font-size:24px" name="demo_div">Hello World!</div>
```

Additionally, you may use these functions on the element to manipulate the attributes. These are necessary if you're attempting to edit 'non-standard' attributes.


- `element.setAttribute(attribute_name, value)`
- `element.getAttribute(attribute_name)`
- `element.hasAttribute(attribute_name)`
- `element.removeAttribute(attribute_name)`


## Input Fields

Similarly, you can also access the values of input fields. You can read more about input fields [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).


```html
<input id="user_input" type="text"/>
<script>
    let text_field = document.getElementById('user_input');
    let user_input = text_field.value;
</script>
```


## Creating and Adding Elements


We can also create elements from scratch.

| function | description |
| ----     | ----        |
| `document.createElement(tag_name)` | create an element with tag `tag_name` |
| `document.createTextNode(text)` | create a text node containing the given text |
| `element.appendChild(child)` | append a child element to a parent element |
| `element.removeChild(child)` | remove a child element from a parent element |
| `element.hasChild(child)` | indicated whether the parent has a particular child |
| `element.replaceChild(child)` | replaces a child |



```html
<div id="container_div"></div>
<script>
    let btn = document.createElement("button");
    btn.style.backgroundColor = "lightblue";
    btn.style.border = "1px solid white";
    btn.innerText = 'click';
    let container_div = document.getElementById('container_div');
    container_div.appendChild(btn);
</script>
```




