from PIL import Image

# # Open the image file
# img = Image.open('myphoto_kangxiaowen.jpg')

# # Convert the image to grayscale
# img_gray = img.convert('L')

# # Save the grayscale image
# img_gray.save('myphoto_kangxiaowen_gray.jpg')


from PIL import Image

# Open the template image and get its size
template = Image.open('prof_pic_bk.jpg')
width, height = template.size

# Open the image to be cropped
img = Image.open('headshot_xiaowenkang_bigsize.jpg')

# Compute the coordinates of the center of the image
center_x = img.width // 2
center_y = img.height // 2

# Compute the coordinates of the top-left and bottom-right corners of the cropping box
left = center_x - width // 2
top = center_y - height // 2
right = center_x + width // 2
bottom = center_y + height // 2

# Crop the image
img_cropped = img.crop((left, top, right, bottom))

# Save the cropped image
img_cropped.save('myphoto_xiaowenkang_cropped.jpg')
