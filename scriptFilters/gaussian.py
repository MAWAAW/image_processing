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
#python filtre_gaussian_YUV.py tigre.png 2 reflect 0.02 pepper


fimage= str(sys.argv[1])
sizeSigma = int(sys.argv[2])
modeBorders = str(sys.argv[3])#{reflect,constant','nearset','mirror','wrap'}
noise_dosage = float(sys.argv[4])#ex 0.05
modeNoise = str(sys.argv[5]) # mode = gaussian, poisson, pepper, salt, s&p, speckle
num_image = str(sys.argv[6])

#Filter gaussian
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
		
	sc.imsave(nameimage+"_gaussianNoisy"+num_image+"."+formatimage,imgbruitee)
	img_noise=scipy.ndimage.imread(nameimage+"_gaussianNoisy"+num_image+"."+formatimage)

	img_out= cv2.cvtColor(img_noise, cv2.COLOR_BGR2YUV)
	Y = img_out[:,:,0]
	U = img_out[:,:,1]
	V = img_out[:,:,2]

	gaussian = scipy.ndimage.filters.gaussian_filter(Y,sigma=sizeSigma,mode=modeBorders)
	
	img_YUV=(np.dstack([gaussian,U,V])).astype(np.uint8)
	img_out_rgb= cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)

	
	sc.imsave(nameimage+"_gaussianFilter"+num_image+"."+formatimage,img_out_rgb)

	#Histogram
	color = ('b','g','r')
	for channel,col in enumerate(color):
	    histr = cv2.calcHist([img_out_rgb],[channel],None,[256],[0,256])
	    plt.plot(histr,color = col)
	    plt.xlim([0,256])
	plt.title('Histogram')
	plt.savefig(nameimage+"_histogram"+num_image+".png")


	
if(X1.ndim==2):

	gaussian = scipy.ndimage.filters.gaussian_filter(imgbruitee,sigma=sizeSigma,mode=modeBorders)
	#Histogram
	plt.hist(gaussian,histtype='barstacked')
	plt.title("Histogram")
	plt.savefig(nameimage+"_histogram"+num_image+".png")

	#save filtered image and noisy image
	sc.imsave(nameimage+"_gaussianFilter"+num_image+"."+formatimage,gaussian)
	sc.imsave(nameimage+"_gaussianNoisy"+num_image+"."+formatimage,imgbruitee)



