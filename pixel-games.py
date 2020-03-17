import numpy as np
from PIL import Image as PImage
from matplotlib import pyplot

# read the input image and obtain the canvas size
inputfile = "renoir.jpg"
width, height = PImage.open("input/"+inputfile).size
imagematrix = pyplot.imread("input/"+inputfile)
x = (width * height)
# since the shape is (3x3x3) we need to reshape it as (x,3) where x is the canvas size (width * height)
flatmatrix = np.reshape(imagematrix,(x,3))
# order by RGB
# sorting we get the indices then apply them to our array
# 0 for red, 1 for green, 2 for blue
ind = np.argsort(flatmatrix[:,0])
ind = flatmatrix[ind]
# reshape the matrix as the original image
imagematrix = np.reshape(ind,(height,width,3))
# show the image
pyplot.imshow(imagematrix)
pyplot.show()
# save the image on disk
img = PImage.fromarray(imagematrix)
img.save("output/"+inputfile, quality=100)
