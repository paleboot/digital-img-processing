from PIL import Image
from PIL import ImageFilter

img = Image.open("./scenery.jpeg")
gamma = 0.3
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        pixelValue = img.getpixel((i,j))

        gammaCorrection = 1/gamma
        redValue = pixelValue[0]/255
        greenValue = pixelValue[1]/255
        blueValue = pixelValue[2]/255

        newRed = 255 * (redValue ** gammaCorrection)
        newGreen = 255 * (greenValue ** gammaCorrection)
        newBlue = 255 * (blueValue ** gammaCorrection)

        img.putpixel((i,j),(int(newRed), int(newGreen),int(newBlue)))
img.show()
img.save("./scenery_gamma<1.jpeg")