from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageOps


img = Image.open('hazelnut333.png')
img_4 = Image.open('breakfast333.webp')


img_6 = Image.new("RGB", (1600, 400))
img_6.paste(img_4, (0, 0))
img_6.paste(img, (800, 0 ))

img_6 = img_6.filter(ImageFilter.GaussianBlur(radius=9))

draw = ImageDraw.Draw(img_6)

font = ImageFont.load_default()     # не будет возможности отрегулировать размер шрифта
text = "Hello, World! "

margin = 10
text_width = draw.textlength(text, font)
draw.text((800 - margin - text_width, 200 - margin ), text=text, font=font)
# img_6.show()

# ImageOps - может перевернуть, транспонировать
img_6 = ImageOps.flip(img_6)    # перевернуть
img_6.show()

img_6 = ImageOps.mirror(img_6)    # зеркальное отображение
img_6.show()

img_6 = ImageOps.posterize(img_6, 4)    # изменить глубину цвета, 8 - хорошо, 1 - плохо
img_6.show()