import sys
import numpy as np
import scipy.ndimage
import scipy.misc
import scipy.stats
import skimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as clrs
import Image
import pylab as P
import colorsys

# image.jpg 3 mirror false

imageLien = str(sys.argv[1])
sizeMatrix = int(sys.argv[2])
modeBorders = str(sys.argv[3])  # {reflect, constant, nearest, mirror, wrap}
booleanNoise = str(sys.argv[4])
modeNoise = str(sys.argv[5])
formatImage = imageLien.split(".")[1]

uploadedImage = scipy.misc.imread(imageLien)

imageT = None
originalArray = np.asarray(Image.open(imageLien))
filtredArray = None
differenceArray = None

shape = uploadedImage.shape  # nombre de lignes, colones et canal
noisyAdd = np.zeros(shape, dtype=np.uint8)
noisyAdd.fill(255)

if booleanNoise == "true" :
    # mode = gaussian , localvar, poisson, pepper, s&p, speckle
    noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True)
    scipy.misc.imsave('static/uploads/MedianFilterNoisy.%s' % formatImage, noisyImage)
    imageT = scipy.ndimage.median_filter(noisyImage, size=sizeMatrix, mode=modeBorders)

elif booleanNoise == "false" :
    # choosenImage = clrs.rgb_to_hsv(uploadedImage)
    imageT = scipy.ndimage.median_filter(uploadedImage, size=sizeMatrix, mode=modeBorders)
    # imageT = clrs.hsv_to_rgb(imageT)
    filtredArray = np.asarray(imageT)

    for i in range(shape[0] - 1):
        for j in range(shape[1] - 1):
            difference = originalArray[i, j][1] - filtredArray[i, j][1]
            if difference < -20 or difference > 20:
                noisyAdd[i, j][0] = originalArray[i, j][0]
                noisyAdd[i, j][1] = originalArray[i, j][1]
                noisyAdd[i, j][2] = originalArray[i, j][2]
    scipy.misc.imsave('MedianFilterNoisy.%s' % formatImage, noisyAdd)

scipy.misc.imsave('static/uploads/MedianFilter.%s' % formatImage, imageT)
plt.hist(imageT, histtype='barstacked')
plt.savefig('static/uploads/histogram.png')
