# import PIL
from PIL import Image

f = 'webp'
# open file 
img = Image.open('check-img.png')
img.show()
# check? that it is img
# move to webp
# img = img.convert('RGB')
# img.show()
# save
name = img.filename
name = name.split('/')[-1].split('.')[0]
print(name)
img.save(f'{name}.{f}', f, optimize = True, quality = 70 )