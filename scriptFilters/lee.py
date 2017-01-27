import sys
import scipy.misc
import skimage
from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.measurements import variance
import matplotlib.pyplot as plt


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

    nameImage, formatImage = imageLien.split(".")

    uploadedImage = scipy.misc.imread(imageLien)

    if modeNoise == "gaussian" or modeNoise == "speckle":
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, var=noise_dosage)
    elif modeNoise == "salt" or modeNoise == "pepper" or modeNoise == "salt & pepper":
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True, amount=noise_dosage)
    else:
        noisyImage = skimage.util.random_noise(uploadedImage, mode=modeNoise, seed=None, clip=True)

    scipy.misc.imsave(nameImage + '_leeNoisy' + num_image + '.' + formatImage, noisyImage)

    imageFiltred = lee_filter(noisyImage,sizeMatrix,modeBorders)
    scipy.misc.imsave(nameImage+'_LeeFilter'+num_image+'.%s'%formatImage, imageFiltred)
    plt.hist(imageFiltred.ravel(),histtype='barstacked')
    plt.savefig(nameImage+'histogram'+num_image+'.png')