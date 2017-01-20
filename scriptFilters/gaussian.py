import sys
import numpy
import scipy.ndimage
import matplotlib.pyplot as plt
from  matplotlib.pyplot import *
import scipy.misc as sc

#python filtre_gaussian.py image.png 2 mirror

fimage= str(sys.argv[1])
sizeSigma = int(sys.argv[2])
modeBorders = str(sys.argv[3])#{reflect,constant','nearset','mirror','wrap'}

#Filter Gaussian
X1 = scipy.ndimage.imread(fimage)
nameimage=fimage.split(".")[0]
formatimage=fimage.split(".")[1]

red = X1[:,:,0]
green = X1[:,:,1]
blue = X1[:,:,2]
X1 = red*1.0

gaussian = scipy.ndimage.filters.gaussian_filter(X1,sigma=sizeSigma,mode=modeBorders)

#Histogram
plt.hist(gaussian,histtype='barstacked')
plt.title("Histogram")
plt.savefig(nameimage+"_histogram.png")


#Noise between two images
l=X1.shape[0]
c=X1.shape[1]
Diff=X1.copy()
for i in range(l):
	for j in range(c):
		Diff[i][j]=X1[i][j]-gaussian[i][j]


#save filtered image and noisy image
sc.imsave(nameimage+"_gaussianFilter."+formatimage,gaussian)
sc.imsave(nameimage+"_gaussianNoisy."+formatimage,Diff)




