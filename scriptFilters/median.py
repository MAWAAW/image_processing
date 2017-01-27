import sys
import numpy as np
import scipy.ndimage
import scipy.misc
import scipy.stats
import skimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import Image


# image.jpg 3 mirror false

imageLien = str(sys.argv[1])
sizeMatrix = int(sys.argv[2])
modeBorders = str(sys.argv[3])  # {reflect, constant, nearest, mirror, wrap}
noise_dosage = float(sys.argv[4])
modeNoise = str(sys.argv[5]) # mode = gaussian, poisson, pepper, s&p, speckle
num_image = str(sys.argv[6])
formatImage = imageLien.split(".")[1]
nameImage = imageLien.split(".")[0]

uploadedImage = scipy.misc.imread(imageLien)

imageT = None
originalArray = np.asarray(Image.open(imageLien))
filtredArray = None
differenceArray = None

shape = uploadedImage.shape  # nombre de lignes, colones et canal
noisyAdd = np.zeros(shape, dtype=np.uint8)
noisyAdd.fill(255)

if modeNoise == "gaussian" or modeNoise == "speckle" :
    noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, var=noise_dosage)
elif modeNoise == "salt" or modeNoise == "pepper" or modeNoise == "salt & pepper" :
    noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, amount=noise_dosage)
else : noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True)

scipy.misc.imsave(nameImage+'_medianNoisy'+num_image+'.'+formatImage, noisyImage)
imageT = scipy.ndimage.median_filter(noisyImage, size=sizeMatrix, mode=modeBorders)

scipy.misc.imsave(nameImage+'_medianFilter'+num_image+'.'+formatImage, imageT)
plt.hist(imageT.ravel(), histtype='barstacked')
plt.savefig(nameImage+'_histogram'+num_image+'.png')