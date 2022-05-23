import image
p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

# img = image.Image("first.gif")

# print(img.getWidth())
# print(img.getHeight())

# p = img.getPixel(45, 55)
# print(p.getRed(), p.getGreen(), p.getBlue())