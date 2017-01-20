import sys
import numpy
import scipy.ndimage
import matplotlib.pyplot as plt
from  matplotlib.pyplot import *
import scipy.misc as sc

#python moyenneur.py image.png 7 constant

fimage= str(sys.argv[1])
sizemasq=int(sys.argv[2])#3x3,5x5,...,49x49
modeBorders = str(sys.argv[3])#{reflect,constant,nearest,mirror, wrap}

#Filter moyenneur
X1 = scipy.ndimage.imread(fimage)
nameimage=fimage.split(".")[0]
formatimage=fimage.split(".")[1]

print(X1.shape)

#Pour voir son effet, on prend la couche rouge d'une image en couleur
red = X1[:,:,0]
green = X1[:,:,1]
blue = X1[:,:,2]
X1 = red*1.0

h=numpy.ones((sizemasq,sizemasq))*1.0/(sizemasq*sizemasq)
#X1:input array to filter

#scipy.ndimage.convolve(input, weights, output=None, mode='reflect', cval=0.0, origin=0)
moyenneur=scipy.ndimage.convolve(X1,h,mode=modeBorders)


#Histogram
plt.hist(moyenneur,histtype='barstacked')
plt.title("Histogram")
plt.savefig(nameimage+"_histogram.png")

#Noise between two images
l=X1.shape[0]
c=X1.shape[1]
Diff=X1.copy()
for i in range(l):
	for j in range(c):
		Diff[i][j]=X1[i][j]-moyenneur[i][j]


#save filtered image and noisy image
sc.imsave(nameimage+"_moyenneurFilter."+formatimage,moyenneur)
sc.imsave(nameimage+"_moyenneurNoisy."+formatimage,Diff)




