
# Lab 9: Clock

Make a clock that displays the current time and updates every second. Check out [JavaScript timing events](https://www.w3schools.com/js/js_timing.asp) and [dates](https://www.w3schools.com/jsref/jsref_obj_date.asp). Writing `new Date()` creates a date with the current date and time. You can then create a string from that date, and set it in the DOM.

## Version 2
Next make a stopwatch. Start with a button that says 'start'. You can then create a `date` to keep track of the time, and use `setHours(0,0,0,0)`. This function will set the date's time to 0 hours, 0 minutes, 0 seconds, and 0 milliseconds. Then set an interval to add 1 to the seconds of that date every second, and show the time in an html element. Add a 'lap' button which takes takes the current time and shows it in a separate list. E.g.

- Lap 1: 00:01:03
- Lap 2: 00:02:34
- Lap 3: 00:04:21

## Version 3 (optional)

Next make a countdown timer. The countdown timer should have a text input for the time, and a drop-down list for the units (seconds, minutes, hours). Set an interval which will start a `date` at the given time, and decrement the seconds each second. The countdown timer should alert the user when it's finished (using an `alert("time's up")` or changing the background color, etc).

There should be controls on the page to switch between the clock, stopwatch, and countdown timer (hint: `display:none` or `$('#the_div').hide() and .show()` if using jQuery).

## Version 4 (optional)

Use animations when switching between the clock, stopwatch, and countdown timer (slide in/out, fade in/out).

