
# Lab 10: Bouncing Block



Let's use an HTML canvas and an animation loop to draw a bouncing block. Create an HTML page with a `canvas element`, preferably with a border so you can see the boundaries. Canvases require that `width` and `height` be set as attributes, rather than though CSS.

`<canvas width="500" height="500"></canvas>`

Use the following to define a 'block' object. The attributes `px` and `py` represent the block's location, and are initialized to a random place on the canvas, `width` and `height` are the dimensions of the canvas. The attributes `vx` and `vy` represent the block's velocity.

```JavaScript
let block = {
    width: 4,
    height: 4,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};
```

We can draw the block by getting the 2D rendering context for the canvas. For more info about drawing, check [here](https://www.w3schools.com/tags/ref_canvas.asp).

```JavaScript
let cnv = document.getElementById('cnv');
let ctx = cnv.getContext("2d");
ctx.clearRect(0, 0, cnv.width, cnv.height);
ctx.fillStyle = "#000000";
ctx.fillRect(block.px, block.py, block.width, block.height);
```

We'll use `requestAnimationFrame` to update the block's position and re-draw it each frame. You can detect when a block hits a side when its x-position or y-position goes beyond the boundaries of the canvas. When this happens, reset its location to be within the boundaries, and negate its velocity depending on which side it hit. When the block hits the left or right side, negate its x-velocity. When the block hits the top or bottom side, negate its y-velocity. This will cause it to "bounce" off the sides.

```JavaScript
function main_loop() {
    // update the block's position
    // check if it hit a boundary
    // draw the block
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);
```

## Version 2

- Draw a circle instead of a block, you'll have to define `center_x` and `center_y`:

```JavaScript
ctx.beginPath();
ctx.arc(center_x, center_y, radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();
```

- Add some gravity, which is a constant downward acceleration. We can represent this by a constant value we add to the ball's y-velocity each frame.

- Also add some friction. Each time the ball makes contact with a boundary, try multiplying its x-velocity and y-velocity by 0.99. This means each time it hides a side, it'll lose 1% of its velocity.

## Version 3 (other options)

- don't redraw the background each phase, this will result in a cool 'streaking' effect

- add multiple balls, each with their own radius, and mass (which would effect their acceleration)

- have balls bounce off of eachother ([link](https://gamedevelopment.tutsplus.com/tutorials/when-worlds-collide-simulating-circle-circle-collisions--gamedev-769))

- Add gravitational attraction between balls: the acceleration due to gravity can be calculated using [Newton's Universal Law of Gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation#Modern_form)
