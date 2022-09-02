from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur", 'png')  # Use PNG because PNG supports filter 

# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("smooth", 'png')

# Convert Img to black and white
filtered_img = img.convert('L')
filtered_img.save('grey.png','png')

# Rotate Image
crooked = filtered_img.rotate(90)
crooked.save('rotate.png', 'png')

# Resize image
resize = filtered_img.resize((200,200))
resize.save('resize.png','png')

# Crop img
box = (100,100,400,400)
crop = filtered_img.crop(box)
crop.save('crop.png','png')

