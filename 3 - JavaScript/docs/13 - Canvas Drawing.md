

# Canvas Drawing


Canvas elements were introduced with HMTL5 and give you complete control over the colors and shapes that occur within it. You can find more info [here](https://www.w3schools.com/graphics/canvas_reference.asp) and [here](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial). Canvas elements **must** have `width` and `height` attributes.


```html
<canvas id="cnv" width="500" height="500"></canvas>
<script>
    let cnv = document.getElementById('cnv');
    let ctx = cnv.getContext('2d');
    ctx.fillStyle = 'green';
    ctx.fillRect(10, 10, 100, 100);
</script>
```

## Rectangles

- `clearRect(x, y, w, h)` clears a rectangle of all colors
- `fillRect(x, y, w, h)` fills in a rectangle
- `strokeRect(x, y, w, h)` draws the outline of a rectangle
- `rect(x, y, w, h)` creates a rectangle, which can then be followed up by `fill()` or `stoke()`

## Circles

```javascript
ctx.beginPath();
ctx.arc(100, 100, 20, 0, 2*Math.PI, false);
ctx.strokeStyle = 'white';
ctx.stroke();
```

## Lines

```javascript
ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(300,150);
ctx.stroke();
```

## Text

- `font` allows you to specify the font to be used
- `fillText(text, x, y)` draws filled-in text
- `strokeText(text, x, y)` draws the outline of text
- `measureText(text)` measures the size of text

```javascript
ctx.font = "30px Arial";
ctx.fillText("Hello World", 10, 50);
```

## Accessing Pixels Directly

If you need direct access to the pixel values, you can 

```javascript
let cnv = document.createElement('canvas');
let ctx = cnv.getContext('2d');
let img = ctx.createImageData(cnv.width, cnv.height);
for (let i=0; i<cnv.width; ++i) {
  for (let j=0; j<cnv.height; ++j) {
    
    let r = 0;
    let g = 0;
    let b = 255;
    let a = 255;
    
    let k = 4*(j + i*cnv.height);
    img.data[k] = r;
    img.data[k+1] = g;
    img.data[k+2] = b;
    img.data[k+3] = a;
  }
}

ctx.putImageData(img, 0, 0);
```




