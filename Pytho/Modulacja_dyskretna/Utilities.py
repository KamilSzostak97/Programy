import matplotlib.pyplot as plt
import numpy as np

def Binary(string,switch):
    if (switch == 0):
        bin = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8'))
        bin = list(map(int, bin))
        #print('variant=littleEndian\n','conversion of ', string,' to binary is equal to [ ', bin,' ]')
        return bin
    else:
        rev=string[::-1]
        bin2 = ''.join(format(i, 'b') for i in bytearray(rev, encoding ='utf-8'))
        bin2 = list(map(int, bin2))
        #print('variant=BigEndian\n','conversion of ', string,' to binary is equal to [ ',''.join(bin2),' ]')
        return bin2

def Wykres(Spot,title,xcords,ycords):
    if(isinstance(Spot,list)):
        plt.subplot(Spot[0],Spot[1],Spot[2])
    else:
        plt.subplot(Spot)
    plt.title(title)
    plt.plot(xcords,ycords)

def Wykres_xlim(Spot,title,xlim,xcords,ycords):
    if(isinstance(Spot,list)):
        plt.subplot(Spot[0],Spot[1],Spot[2])
    else:
        plt.subplot(Spot)
    plt.xlim(xlim[0],xlim[1])
    plt.title(title)
    plt.plot(xcords,ycords)

def Spectrum(ycords):
    spectrum = np.fft.rfft(ycords)
    xcords = np.linspace(0,1,len(spectrum))
    return xcords,spectrum

def bandwidth(A):
    X=np.amax(A)
    Y=np.amin(A)
    return (abs(abs(X)-abs(Y)))
