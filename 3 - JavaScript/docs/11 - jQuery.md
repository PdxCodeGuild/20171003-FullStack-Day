
# jQuery

[jQuery](https://jquery.com/) is a JavaScript library that can make general DOM manipulation easier, enables some operations that are difficult in 'Vanilla' JS, and standardizes cross-browser compatibility. It's still very popular (and thus worth familiarizing yourself with), but it was more useful in the past. JavaScript got better, and front-end frameworks like Angular, Reach, and Vue emerged. You shouldn't build complex pages using jQuery because they quickly become unmanageable, but it's still very common and useful for simpler pages. You can learn more about jQuery [here](https://learn.jquery.com/) and [here](https://www.w3schools.com/jquery/default.asp). There's also [jQuery Mobile](http://jquerymobile.com/) and [jQuery UI](https://jqueryui.com/).


You can include jQuery by adding the following tag in your `head`.

```html
<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>
```

## Executing code on page load

Without jQuery:
```javascript
window.onload = function() {
  console.log('ready!');
};
```

With jQuery:
```javascript
$(document).ready(function() {
  console.log('ready!');
});
```

Or more succinctly:
```javascript
$(function() {
  console.log('ready!');
});
```


## Selecting Elements

One major advantage of jQuery is that it simplifies the selection of elements, and enable you to use CSS selectors. Note that these return special jQuery objects, which are wrapped around the Vanilla JS objects. You can find more about selectors [here](http://api.jquery.com/category/selectors/5 - jQuery.md).

```javascript
$('#header'); // select the element with an ID of 'header'
$('li');      // select all list items on the page
$('ul li');   // select list items that are in unordered lists
$('.person'); // select all elements with a class of 'person'
```

## Getting and Setting Values

### HTML

```javascript
// get the innerHTML on every li element
$('li').html();
```

```javascript
// set the innerHTML on every li element
$('li').html('New HTML');
```

```javascript
// add explanation points to the innerHTML of every li element
$('li').html(function( index, oldHtml ) {
  return oldHtml + '!!!'
});
```
```javascript
// iterate through each li element
$( 'li' ).each(function(index, elem) {
  // this: the current, raw DOM element
  // index: the current element's index in the selection
  // elem: the current, raw DOM element (same as this)
  $( elem ).prepend( '<b>' + index + ': </b>' );
});
```

### Attributes

```javascript
// set the disabled attribute on all inputs
$("input").attr("disabled", true);
$("input").attr('disabled', 'disabled');

//remove it
$("input").removeAttr("disabled");
```

### CSS

```javascript
// add the css class 'red'
$('li').addClass('red');

// remove the css class 'red'
$('li').removeClass('red');

// set a css property
$('li').css({
    color: 'red'
});

// hide an element
$('li').hide();
```

## Events

```javascript
$("p").click(function(){
  // action goes here!!
});

$("p").dblclick(function(){
    $(this).hide();
});

$("#p1").mouseenter(function(){
    alert("You entered p1!");
});

$("#p1").mouseleave(function(){
    alert("You left p1!");
});

$("#p1").mousedown(function(){
    alert("Mouse down over p1!");
});

$("#p1").mouseup(function(){
    alert("Mouse up over p1!");
});

$("p").on({
    mouseenter: function(){
        $(this).css("background-color", "lightgray");
    }, 
    mouseleave: function(){
        $(this).css("background-color", "lightblue");
    }, 
    click: function(){
        $(this).css("background-color", "yellow");
    } 
});
```

## Animation

```javascript
$('li').fadeIn();

$('li').animate({
    left: '+=100'
});
```

## AJAX

```javascript
$.ajax({
    url: 'http://example.com'
})
.done(function (data) {
    alert(data);
});
```
