import matplotlib
import numpy
from PIL import Image
import scipy
import math
from scipy.misc import toimage


image=Image.open('lena_gray.png')
width, height = image.size
print (width)
print (height)

im=numpy.array(Image.open('lena_gray.png'))

h = []

for i in range(256):
    h.append(0)

g = []

for i in range(256):
    g.append(0)

t = []

for i in range(256):
    t.append(0)


for x in range (0,width-1):
    for y in range (0, height-1):
        h[im[x,y]]=h[im[x,y]]+1

g[0]=h[0]
for x in range (1,255):
    g[x]=g[x-1]+h[x]


for x in range (0,255):
    t[x]=math.floor(255*g[x]/(width*height))

image1 = numpy.zeros(shape=(width, height), dtype=int)
image1 = numpy.array(image1)


for x in range (0,width-1):
    for y in range (0, height-1):
        image1[x,y]=t[im[x,y]]


toimage(im).save('OriginalImage.png')
toimage(image1).save('EnhancedImage.png')
