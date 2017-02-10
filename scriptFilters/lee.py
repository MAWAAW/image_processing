import sys
import scipy.misc
import numpy as np
import skimage
from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.measurements import variance
import matplotlib.pyplot as plt
import cv2


def lee_filter(img, size,modeBorders):
    mean = uniform_filter(img, size,mode=modeBorders)
    pow2_mean = uniform_filter(img**2, size,mode=modeBorders)
    mean_variance = pow2_mean - mean**2
    variance_speckle = variance(img)
    img_weights = mean_variance**2 / (mean_variance**2 + variance_speckle**2) # W = O2 / (O2 + o2)
    img_filtred = mean + img_weights * (img - mean) # L = M + W*(C-M)
    return img_filtred

if __name__ == '__main__':
    imageLien = str(sys.argv[1])
    sizeMatrix = int(sys.argv[2])
    modeBorders = str(sys.argv[3])
    num_image = str(sys.argv[4])
    modeNoise = str(sys.argv[5])  # mode = gaussian, poisson, pepper, s&p, speckle
    noise_dosage = float(sys.argv[6])

    imageFiltred = None

    nameImage, formatImage = imageLien.split(".")

    uploadedImage = scipy.misc.imread(imageLien)

    if modeNoise == "gaussian" or modeNoise == "speckle":
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, var=noise_dosage)
    elif modeNoise == "salt" or modeNoise == "pepper" or modeNoise == "salt & pepper":
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, amount=noise_dosage)
    else:
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True)

    scipy.misc.imsave(nameImage + '_leeNoisy' + num_image + '.' + formatImage, noisyImage)

    img_noisyImage = scipy.misc.imread(nameImage + '_leeNoisy' + num_image + '.' + formatImage)

    if (uploadedImage.ndim == 3):
        img_out = cv2.cvtColor(img_noisyImage, cv2.COLOR_BGR2YUV)
        y = img_out[:, :, 0]
        u = img_out[:, :, 1]
        v = img_out[:, :, 2]

        yT = lee_filter(y,sizeMatrix,modeBorders)

        img_YUV = (np.dstack([yT, u, v])).astype(np.uint8)
        imageFiltred = cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR, 3)

        color = ('b', 'g', 'r')
        for channel, col in enumerate(color):
            hist = cv2.calcHist([imageFiltred], [channel], None, [256], [0, 256])
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
        plt.savefig(nameImage + 'histogram' + num_image + '.png')

    else:
        imageFiltred = lee_filter(noisyImage,sizeMatrix,modeBorders)
        plt.hist(imageFiltred.ravel(), histtype='barstacked')
        plt.savefig(nameImage + 'histogram' + num_image + '.png')

scipy.misc.imsave(nameImage+'_LeeFilter'+num_image+'.%s'%formatImage, imageFiltred)
'''
    imageFiltred = lee_filter(noisyImage,sizeMatrix,modeBorders)
    scipy.misc.imsave(nameImage+'_LeeFilter'+num_image+'.%s'%formatImage, imageFiltred)
    plt.hist(imageFiltred.ravel(),histtype='barstacked')
    plt.savefig(nameImage+'histogram'+num_image+'.png')
'''