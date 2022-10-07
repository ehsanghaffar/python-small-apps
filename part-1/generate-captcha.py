
from captcha.image import ImageChaptcha

# specify img size
img = ImageChaptcha(width=300, height=100)

# specify text for chaptcha
captcha_txt = input("Enter text for Captcha: ")

# genetate img from text
data = img.generate(captcha_txt)

# write img on file and save
img.write(captcha_txt, 'captcha.png')


# see the captcha image
from PIL import Image
Image.open('captcha.png')