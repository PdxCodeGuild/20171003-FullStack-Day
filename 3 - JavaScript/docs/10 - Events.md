
# Events

You can find out more info [here](https://developer.mozilla.org/en-US/docs/Web/Events).

## Defining Events

The easiest (but least recommended) way to define an event is inside the attribute of a tag. This is problematic because writing a significant amount of JavaScript will make the HTML difficult to read. Even if it's only a little JavaScript, you'd be running JavaScript in both your attributes and your script tag, which is difficult to keep track of.

```html
<button id="bt" onclick="alert('hello world!');">click</button>
```

A much better way is to assign the event attribute as a function in your script tag.


```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.onclick = function() {
        alert('hello world!');
    }
</script>
```

A third way, which is useful if you'll have different functions triggered by the same event, is to use **listeners**. More info [here](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener).

```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.addEventListener('click', function() {
        alert('hello world!');
    });
</script>
```

## List of Events

You can find a comprehensive list of events [here](https://developer.mozilla.org/en-US/docs/Web/Events).



### Various Events


```javascript
window.onload = function() {
    // here it's safe to access DOM elements
    // because everything on the page has been loaded
}
```

```html
<input id="txt" type="text"/>
<script>
    let txt = document.getElementById('txt');
    txt.onchange = function() {
        console.log(txt.value);
    }
</script>

```



### Focus Events

| function | description |
| ----     | ----        |
| `focus` | when an element has focus |
| `blur` | when an element loses focus |


```javascript

```


### Keyboard Events

| function | description |
| ----     | ----        |
| `keydown` | any key is pressed |
| `keyup` | any key is released |
| `keypress` | any button except Shift, Fn, CapsLock is pressed (fires continuously) |

```
<script>
    document.body.onkeydown = function(evt) {
      alert(evt.keyCode);
    }
</script>
```


### Mouse Events


| function | description |
| ----     | ----        |
| `mouseenter` | the mouse has entered the element |
| `mouseleave` | the mouse has left the element
| `mousemove` | the mouse has moved on the element |
| `mousedown` | the mouse has been pressed |
| `mouseup` | the mouse has been released |
| `click` | the mouse has been pressed and released |

The event parameter that's passed to the function contains the coordinates of the mouse, and which button is pressed.

```javascript
<canvas id="cnv" width="100" height="100"></canvas>
<script>
let cnv = document.getElementById('cnv');
dnv.onclick = function(event) {
    var x = event.clientX;
    var y = event.clientY;
    alert('position: '+x+', '+y+'\nbutton: '+button);
}
</script>
```
