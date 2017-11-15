

# Canvas Drawing


Canvas elements were introduced with HMTL5 and give you complete control over the colors and shapes that occur within it. Canvas elements **must** have `width` and `height` attributes.


```html
<canvas width="500" height="500"></canvas>
<script>
    let cnv = document.getElementById('tutorial');
    
    let ctx = cnv.getContext('2d');
    ctx.fillStyle = 'green';
    ctx.fillRect(10, 10, 100, 100);
    
</script>
```

## Drawing a Rectangle


```javascript
let ctx = cnv.getContext('2d');
ctx.rect(20, 20, 150, 100);
ctx.stroke();
```

## Writing Text

```javascript
var cnv = document.getElementById("cnv");
var ctx = cnv.getContext("2d");
ctx.font = "30px Arial";
ctx.fillText("Hello World", 10, 50);
```


## Drawing a Line

```javascript
var cnv = document.getElementById("cnv");
var ctx = cnv.getContext("2d");
ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(300,150);
ctx.stroke();
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




