import sys
import numpy
import scipy.ndimage
import matplotlib.pyplot as plt
from  matplotlib.pyplot import *
import scipy.misc as sc
from skimage.util import random_noise
import skimage
from skimage.color import *
import cv2
#python filtre_moyenneur_YUV.py tigre.png 7 constant 0.02 gaussian

fimage= str(sys.argv[1])
sizemasq=int(sys.argv[2])#3x3,5x5,...,49x49
modeBorders = str(sys.argv[3])#{reflect,constant,nearest,mirror, wrap}
noise_dosage = float(sys.argv[4])#ex 0.05
modeNoise = str(sys.argv[5]) # mode = gaussian, poisson, pepper, salt, s&p, speckle
num_image = str(sys.argv[6])

#Filter moyenneur
X1 = scipy.ndimage.imread(fimage)
nameimage=fimage.split(".")[0]
formatimage=fimage.split(".")[1]

#add noise to original image
if modeNoise == "gaussian" or modeNoise == "speckle" :
    imgbruitee = skimage.util.random_noise(X1, mode=modeNoise, seed=None, clip=True, var=noise_dosage)
elif modeNoise == "salt" or modeNoise == "pepper" or modeNoise == "s&p" :
    imgbruitee = skimage.util.random_noise(X1, mode=modeNoise, seed=None, clip=True, amount=noise_dosage)
else : imgbruitee = skimage.util.random_noise(X1, mode=modeNoise, seed=None, clip=True)


if(X1.ndim==3):
		
	sc.imsave(nameimage+"_moyenneurNoisy"+num_image+"."+formatimage,imgbruitee)
	img_noise=scipy.ndimage.imread(nameimage+"_moyenneurNoisy"+num_image+"."+formatimage)

	img_out= cv2.cvtColor(img_noise, cv2.COLOR_BGR2YUV)
	Y = img_out[:,:,0]
	U = img_out[:,:,1]
	V = img_out[:,:,2]

	h=numpy.ones((sizemasq,sizemasq))*1.0/(sizemasq*sizemasq)
	
	#scipy.ndimage.convolve(input, weights, output=None, mode='reflect', cval=0.0, origin=0)
	moyenneur=scipy.ndimage.convolve(Y,h,mode=modeBorders)
	
	img_YUV=(np.dstack([moyenneur,U,V])).astype(np.uint8)
	img_out_rgb= cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)

	
	sc.imsave(nameimage+"_moyenneurFilter"+num_image+"."+formatimage,img_out_rgb)

	#Histogram
	color = ('b','g','r')
	for channel,col in enumerate(color):
	    histr = cv2.calcHist([img_out_rgb],[channel],None,[256],[0,256])
	    plt.plot(histr,color = col)
	    plt.xlim([0,256])
	plt.title('Histogram')
	plt.savefig(nameimage+"_histogram"+num_image+".png")


	
if(X1.ndim==2):

	h=numpy.ones((sizemasq,sizemasq))*1.0/(sizemasq*sizemasq)
	moyenneur=scipy.ndimage.convolve(imgbruitee,h,mode=modeBorders)
	#Histogram
	plt.hist(moyenneur,histtype='barstacked')
	plt.title("Histogram")
	plt.savefig(nameimage+"_histogram"+num_image+".png")

	#save filtered image and noisy image
	sc.imsave(nameimage+"_moyenneurFilter"+num_image+"."+formatimage,moyenneur)
	sc.imsave(nameimage+"_moyenneurNoisy"+num_image+"."+formatimage,imgbruitee)



