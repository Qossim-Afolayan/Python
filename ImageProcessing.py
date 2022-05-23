import image
from PIL import Image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

img = image.Image("image-dhabi.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(30, 100) #(column, row)
print(p.getRed(), p.getGreen(), p.getBlue())