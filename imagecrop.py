from PIL import Image

img1 = Image.open('./content/images/TwitterEOY1.png')
img2 = Image.open('./content/images/TwitterEOY2.jpg')

print(img1.size)
print(img2.size)

img1 = img1.resize((700, 450))
img2 = img2.resize((500,200))

print(img1.size)
print(img2.size)

img1.save("./content/images/TwitterEOY1.png", 'png')
img2.save("./content/images/TwitterEOY2.jpg", 'png')