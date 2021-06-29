import numpy, urllib.request
from PIL import Image, ImageDraw, ImageFont


def cropper(choice, image):
    imUrl = urllib.request.urlopen(image)
    imSave = open("logo.png", "wb")
    imSave.write(imUrl.read())
    imSave.close()
    im = Image.open('logo.png').convert('RGB')
    numpyIm = numpy.array(im)
    width, height = im.size
    if choice.upper() == "R":
        imChoice = Image.new('L', im.size, 0)
        imDraw = ImageDraw.Draw(imChoice)
        imDraw.pieslice([0, 0, width, height], 0, 360, fill = 255)
    else:
        imChoice = Image.new('L', im.size, 0)
        imDraw = ImageDraw.Draw(imChoice)
        imDraw.rectangle([0, 0, width, height], fill = 255)
    

    numpyChoice = numpy.array(imChoice)

    numpyDone = numpy.dstack((numpyIm, numpyChoice))

    Image.fromarray(numpyDone).save('logo.png')

def initialsOnImage(initials):
    im = Image.open('logo.png')
    imDraw = ImageDraw.Draw(im)
    imFont = ImageFont.truetype("SEASRN__.ttf", 92)
    width, height = im.size
    W, H = imDraw.textsize(initials, font=imFont)
    imDraw.text(((width - W)/2, (height-H)/2), initials, font = imFont, align="center")
    im.show()
    im.save('logo.png')

        
initials = input("Enter your name initials: ")
choice = input("Enter 'R' if you want round logo or 'S' for squared: ")
image = input("Copy image link: \n")


cropper(choice, image)
initialsOnImage(initials)
