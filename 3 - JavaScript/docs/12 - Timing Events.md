
# Timing Events

Timing events allow us to delay execution of code, or execute code on a fixed interval, which is useful for many things. You can read more about timing events [here](https://www.w3schools.com/js/js_timing.asp) and [here](https://developer.mozilla.org/en-US/Add-ons/Code_snippets/Timers).

## Using setTimeout and clearTimeout

`setTimeout` calls a function after given number of milliseconds passes.

```javascript
setTimeout(function() {
    alert('hi!');
}, 3000); // 3000 milliseconds, or 3 seconds

// this can also be written like this
function timeout_example() {
    alert('hi!');
}
setTimeout(timeout_example, 3000);
```

If you want to cancel the timeout before it's finished, you can pass the `int` returned by `setTimeout` to `clearTimeout`.


```javascript
let interval = setTimeout(function() {
    alert('hi!');
}, 3000);
clearTimeout(interval);
```


## Using setInterval

`setInterval` allows us to execute code repeatedly, until the page is changed or the interval is cleared

```javascript
setInterval(function() {
    alert('hi!');
}, 3000);
```

To stop it, you can pass `clearInterval` the `int` you get from `setInterval`

```javascript
let counter = 0;
let interval = setInterval(function() {
    counter += 1;
    if (counter > 10) {
        clearInterval(interval);
    }
}, 3000);

```


## window.requestAnimationFrame

To have code called 'as often as possible' without locking up the entire page, you can use `window.requestAnimationFrame`.


```html
<div id="moving_div"></div>
<script>
    let moving_div = document.getElementById('moving_div');
    moving_div.style.position = 'absolute';
    moving_div.style.left = 0;
    moving_div.style.top = 0;
    function animation_step() {
        moving_div.style.left += 0.1;
        if (moving_div.style.left < 100) {
            window.requestAnimationFrame(animation_step);
        }
    }
    window.requestAnimationFrame(animation_step);
</script>
```





