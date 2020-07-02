import math
import numpy as np
import matplotlib.pyplot as plt
import array

def Wykres(Spot,title,xlabel,ylabel,xcords,ycords,switch):
    if(isinstance(Spot,list)):
        plt.subplot(Spot[0],Spot[1],Spot[2])
    else:
        plt.subplot(Spot)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if(switch==0):
        plt.plot(xcords,ycords)
    else:
        plt.stem(ycords)

def Main(Ka,Kp):
    xcords = [] ; ycords = [] ; ycords1 = [] ; ycords2 = []
    fm=5;fn=100;a=1;x=0

    while x <= a:
        xcords.append(x)
        MT = 1 * math.sin(2 * math.pi * fm * x)
        ycords.append(MT)
        ZA = (Ka*MT+1)*np.cos(2 * math.pi * fn * x)
        ycords1.append(ZA)
        ZT = np.cos(2 * math.pi * fn * x + Kp*MT)
        ycords2.append(ZT)
        x=x+0.001
        x=round(x,4)
    ZAW = np.fft.rfft(ycords1)
    ZTW = np.fft.rfft(ycords2)

    plt.figure()
    Wykres(511,'Pure tone','Time','Signal Strength',xcords,ycords,0)
    Wykres(512,'AM modulation','Time','Signal Strength',xcords,ycords1,0)
    Wykres(513,'PM modulation','Time','Signal Strength',xcords,ycords2,0)
    plt.subplot(514)

    if 1>Ka>0:
        plt.xlim(90,110);plt.ylim(-50)
        plt.title('AM spectrum')
        plt.xlabel('Frequency');plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)

        plt.subplot(515)
        plt.xlim(90,100);plt.ylim(-250)
        plt.title('PM spectrum')
        plt.xlabel('Frequency');plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)

    if  12>Ka>2:
        plt.xlim(90,110);plt.ylim(-70)
        plt.title('AM spectrum')
        plt.xlabel('Frequency');plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)

        plt.subplot(515)
        plt.xlim(89,96);plt.ylim(-50)
        plt.title('PM spectrum')
        plt.xlabel('Frequency');plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)

    if  Ka>12:
        plt.xlim(90,115) ; plt.ylim(-300)
        plt.title('AM spectrum')
        plt.xlabel('Frequency');plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)

        plt.subplot(515)
        plt.xlim(0,200);plt.ylim(-150)
        plt.title('PM spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)

    pasmo1=[] ; pasmo2=[]
    for i in range(len(ZTW)):
        if(ZTW[i]>=-3):
            pasmo1.append(ycords1[i])
    for i in range(len(ZAW)):
        if(ZAW[i]>=-3):
            pasmo2.append(ycords2[i])
    fmin1=np.min(pasmo1) ; fmin2=np.min(pasmo2)
    fmax1=np.max(pasmo1) ; fmax2=np.max(pasmo2)
    w1 = fmax1-fmin1 ; w2 = fmax2-fmin1

Main(0.5,1.5)
Main(11,1.4)
Main(34,43)
plt.show()
