# Lab 18: Image Manipulation

Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'. If you don't have pillow installed, run `pip install pillow` in a terminal. Use the formula for converting to greyscale and the code below. Remember that Pillow uses `ints` for RGB values, in the range of 0-255, whereas your math will often use `floats`. 

'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.

`Y = 0.299*R + 0.587*G + 0.114*B`

```python
from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here

        pixels[i, j] = (r, g, b)

img.show()

```



## Version 2

Use the `colorsys` library to increase the saturation, decrease the saturation, and rotate the hue. Colorsys represents colors as floats in the range 0.0 - 1.0.

```python
import colorsys

# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# do some math on h, s, v

r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)

```