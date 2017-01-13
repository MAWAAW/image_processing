import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


print "Filtre Median Debut"
image_name = sys.argv[1]

uploadedImage = mpimg.imread(image_name)

print 'LE NOM DE LIMAGE C QUOI????? '+image_name

shape = uploadedImage.shape # nombre de lignes, colones et canal

n_pixel = np.zeros((9)) #tableau de zeros pour l'image non bruitee

row,column,chanel = shape
n_pixel_noisy = np.zeros([row,column,chanel],dtype=np.uint8) #image blanc de bruit
n_pixel_noisy.fill(255)

for i in range(shape[0]-1):
    for j in range(shape[1]-1):
        if j > 0 and i > 0:
            n_pixel[0] = uploadedImage[i-1,j-1,0]
            n_pixel[1] = uploadedImage[i-1,j,0]
            n_pixel[2] = uploadedImage[i-1,j+1,0]
            n_pixel[3] = uploadedImage[i,j-1,0]
            n_pixel[4] = uploadedImage[i,j,0]
            n_pixel[5] = uploadedImage[i,j+1,0]
            n_pixel[6] = uploadedImage[i+1,j-1,0]
            n_pixel[7] = uploadedImage[i+1,j,0]
            n_pixel[8] = uploadedImage[i+1,j+1,0]
            centre = n_pixel[4]
            s = np.sort(n_pixel, axis=None)        
            uploadedImage[i,j,0] = s[4]
            uploadedImage[i,j,1] = s[4]
            uploadedImage[i,j,2] = s[4]
            newCentre = s[4]
            #enregistrer le bruit
            if centre != newCentre :
                n_pixel_noisy[i,j,0] = uploadedImage[i,j,0]
                n_pixel_noisy[i,j,1] = uploadedImage[i,j,1]
                n_pixel_noisy[i,j,2] = uploadedImage[i,j,2]

mpimg.imsave(image_name+'ImageFilter.png', uploadedImage)

mpimg.imsave(image_name+'Noise.png', n_pixel_noisy)


hist = np.histogram(n_pixel_noisy, bins=np.arange(0, 256))
plt.plot(hist[1][:-1], hist[0], lw=2)
plt.title("Histogram")
plt.savefig(image_name+'Histogram.png')
#plt.show()

print "Filtre Median Fin"