
from PIL import Image, ImageDraw
import colorsys


def crop(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    return x


def invert_image():
    img = Image.open("C:\\Users\\simian201\\Desktop\\programs\\20171003-FullStack-Day\\1 - Python\\solutions\\Lenna.png")
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            #di = i - width/2
            #dj = j - height/2
            #d = math.sqrt(di*di + dj*dj)
            #if d < 100:
            #    g = r
            #    b = r

            pixels[i, j] = (255-r, 255-g, 255-b)

    img.show()


def crazy_stuff():
    img = Image.open("Lenna.png")
    width, height = img.size
    pixels = img.load()

    print(type(pixels))

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            if h < 0.5 or h > 0.9:
                s = 0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

    img.show()


def stick_figure():

    width = 400
    height = 400

    img = Image.new('RGB', (width, height))

    draw = ImageDraw.Draw(img)

    # the origin (0, 0) is at the top-left corner

    draw.rectangle(((0, 0), (width, height)), fill="white")

    # draw a line from x0, y0, x1, y1
    # using the color pink
    color = (256, 128, 128)  # pink
    draw.line((250, 100, 250, 300), fill=color)
    draw.line((100, 250, 300, 250), fill=color)
    draw.line((250, 300, 200, 350), fill=color)
    draw.line((250, 300, 300, 350), fill=color)

    # draw a rectangle from x0, y0 to x1, y1
    draw.rectangle(((200, 100), (300, 200)), fill="lightblue")

    circle_x = width / 4
    circle_y = height / 4
    circle_radius = 50
    draw.ellipse(
        (circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius),
        fill='lightgreen')

    img.show()

stick_figure()
