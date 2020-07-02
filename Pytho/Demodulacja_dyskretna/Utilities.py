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

def wartoscProgowa (pt,h):
    wp = []
    for p in pt:
        if p < h:
            wp.append(1)
        else:
            wp.append(0)
    return wp
