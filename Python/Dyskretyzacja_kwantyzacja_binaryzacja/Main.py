import numpy as np
import pandas as pd
import scipy as scp
import math
from scipy import stats, optimize
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from matplotlib import image as img
import numpy as np
from PIL import Image

def Dyskretyzacja(f, fs):
    t=[] ; s=[]
    dt=1/fs ; tn=0
    while tn<=1:
        t.append(tn)
        s.append(math.sin(2*(math.pi)*f*tn))
        tn+=dt
    return [t,s]

fig, axs=plt.subplots(2,5)

[a,b]=Dyskretyzacja(10,20)
axs[0,0].plot(a,b)

[a,b]=Dyskretyzacja(10,21)
axs[0,1].plot(a,b)

[a,b]=Dyskretyzacja(10,30)
axs[0,2].plot(a,b)

[a,b]=Dyskretyzacja(10,45)
axs[0,3].plot(a,b)

[a,b]=Dyskretyzacja(10,50)
axs[0,4].plot(a,b)

[a,b]=Dyskretyzacja(10,100)
axs[1,0].plot(a,b)

[a,b]=Dyskretyzacja(10,150)
axs[1,1].plot(a,b)

[a,b]=Dyskretyzacja(10,200)
axs[1,2].plot(a,b)

[a,b]=Dyskretyzacja(10,250)
axs[1,3].plot(a,b)

[a,b]=Dyskretyzacja(10,1000)
axs[1,4].plot(a,b)

#4 Twierdzenie o próbkowaniu
#5 Aliasing
#6 https://www.pcgamingwiki.com/wiki/Glossary:Anti-aliasing_(AA)#/media/File:Not_antialiased_Cube.png
#7 Python radzi sobie za pomoca rozmazania obrazu za pomoca interpolacji

#Kwantyzacja

oa=img.imread('obraz3.png')
ob=img.imread('obraz3.png')
oc=img.imread('obraz3.png')

a,b,c=ob.shape
print("wysokosc: ",a," szerokosc: ",b, "wartosci" ,c)

def GrayMaker(ob):
    r,g,b=ob[:,:,0],ob[:,:,1],ob[:,:,2]
    gray=ob

    for i, row in enumerate(ob):
            for j, pixel in enumerate(row):
                gray[i, j] = (max(pixel) + min(pixel))/2

    return gray

def GrayMaker2(ob):
    r,g,b=ob[:,:,0],ob[:,:,1],ob[:,:,2]
    gray=ob

    for i, row in enumerate(ob):
            for j, pixel in enumerate(row):
                gray[i, j] = (pixel[0]+pixel[1]+pixel[2])/3

    return gray


def GrayMaker3(ob):
    r,g,b=ob[:,:,0],ob[:,:,1],ob[:,:,2]
    gray=ob

    for i, row in enumerate(ob):
            for j, pixel in enumerate(row):
                gray[i, j] = 0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2]

    return gray

def binaryzacja():
    image = plt.imread('obraz3.png')
    image = image[:,:,:3]
    image = GrayMaker(image)
    grayImage = np.dot(image[...,:3], [0.21, 0.72, 0.07])
    fig, axs = plt.subplots(3)
    axs[0].imshow(grayImage, cmap = 'gray')
    axs[1].hist(grayImage.ravel(), bins = 256)
    counts, bins = np.histogram(grayImage.ravel()*255, 2)
    binarizedImage = (grayImage * 255)>bins[1]
    axs[2].imshow(binarizedImage, cmap = 'gray')
    plt.show()

fig, axs=plt.subplots(3,2)

graymade = GrayMaker(ob)
graymade2 = GrayMaker2(ob)
graymade3 = GrayMaker3(ob)

axs1 = np.histogram(graymade.ravel())
axs2 = np.histogram(graymade2.ravel())
axs3 = np.histogram(graymade3.ravel())

axs[0,0].imshow(oc)
axs[0,1].hist(oc.ravel(), bins = 16)

axs[1,0].imshow(graymade)
axs[1,1].hist(graymade3.ravel(), bins = 16)

_ ,bins = np.histogram(oc,4)
img_digitized = np.digitize(oc, bins)
new_img = bins[img_digitized-1]

axs[2,0].imshow(new_img)
axs[2,1].hist(new_img.ravel())

binaryzacja()
