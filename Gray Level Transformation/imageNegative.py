from PIL import Image
from PIL import ImageFilter

img = Image.open("./lamp.jpeg")
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        pixelValue = img.getpixel((i,j))
        redValue = 255 - pixelValue[0]
        greenValue = 255 - pixelValue[1]
        blueValue = 255 - pixelValue[2]

        img.putpixel((i,j), (redValue, greenValue, blueValue))
img.show()
img.save("./lamp_negative.jpeg")