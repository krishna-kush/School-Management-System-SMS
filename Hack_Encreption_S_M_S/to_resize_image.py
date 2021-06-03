import PIL
from PIL import Image

def resize():#for resise aur logo
    basewidth = 700
    img = Image.open('SMS_Title.png')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('sized_SMS_Title.png')

resize()