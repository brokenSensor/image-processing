from PIL import Image
import sys
import os

orig = sys.argv[1]
newfold = sys.argv[2]

try:
    os.mkdir(newfold)
except:
    pass

for imag in os.listdir(orig):
    im = Image.open(".\\"+orig+imag)
    im.save(".\\"+newfold+imag[0:-3]+"png", 'png')
    print("done")
