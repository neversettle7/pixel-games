import numpy as np
from PIL import Image as PImage
from matplotlib import pyplot
inputfile = "renoir.jpg"
width, height = PImage.open("input/"+inputfile).size
imagematrix = pyplot.imread("input/"+inputfile)
x = (width * height)
flatmatrix = np.reshape(imagematrix,(x,3))
#order by RDB
ind = np.argsort(flatmatrix[:,0])
ind = flatmatrix[ind]
imagematrix = np.reshape(ind,(height,width,3))
pyplot.imshow(imagematrix)
pyplot.show()
img = PImage.fromarray(imagematrix)
img.save("output/"+inputfile, quality=100)
