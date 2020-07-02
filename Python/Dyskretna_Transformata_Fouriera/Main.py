
import random
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

def DFT(fnList):
    N = len(fnList)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += fnList[n] * cmath.exp(- 1j * pi2 * m * n / N)
        FmList.append(Fm / N)
    return FmList

def InverseDFT(FmList):
    N = len(FmList)
    fnList = []
    for n in range(N):
        fn = 0.0
        for m in range(N):
            fn += FmList[m] * cmath.exp(1j * pi2 * m * n / N)
        fnList.append(fn)
    return fnList

def spectrum(N):
    X_re = N ; X_im = N ; x = N ; M=N
    X_rer = [] ; X_imi = [] ; EM = []
    N=len(N)
    for k in range(N-1):
        for n in range(N-1):
            X_rer.append(X_re[k]+(x[n]*np.cos((-2*np.pi*k*n)/N)))
            X_imi.append(X_im[k]+(x[n]*np.sin((-2*np.pi*k*n)/N)))

    for k in range(N-1):
        EM.append(np.sqrt(X_re[k]*X_re[k]+X_im[k]*X_im[k]))
    tresh = np.amax(EM)
    for k in range(N-1):
        if(EM[k]<tresh):
            EM[k]=0

    for k in range (N-1):
        EM[k]=10*np.log(M[k])
    return EM

def TonProsty():
    ycords = [];a=1;b=2;c=3;x=0
    while x <= a:
        funkcja = math.sin(2 * math.pi * b * x)
        ycords.append(funkcja)
        x=x+0.03
        x=round(x,2)
    return(ycords)


pi2 = cmath.pi * 2.0
a=4;b=5;c=4;
acords = [] ; ycords = [] ; zcords = [] ; ucords = [] ; pcords = []

x=-10
while x < 10:
    fx = (a * (x * x)) + (b * x) +  c
    acords.append(fx)
    x=x+0.05
    x=round(x,2)

x=0
while x < 1:
    fx = (a * (x * x)) + (b * x) +  c
    funkcja = (2 * (fx * fx)) + (12*math.cos(x))
    ycords.append(funkcja)

    funkcja2 = (math.sin(2*math.pi*7*x)*fx)-0.2*math.log((abs(funkcja)+math.pi),10)
    zcords.append(funkcja2)

    funkcja3 = math.sqrt(abs(funkcja*funkcja*funkcja2))-1.8*math.sin(0.4*x*funkcja2*funkcja)
    ucords.append(funkcja3)
    x=x+0.01
    x=round(x,2)

def Wykres(Spot,title,Data,switch):
    if(isinstance(Spot,list)):
        plt.subplot(Spot[0],Spot[1],Spot[2])
    else:
        plt.subplot(Spot)
    plt.title(title)
    if(switch==0):
        plt.plot(Data)
    else:
        plt.stem(Data)

N=TonProsty()
Wykres(341,'Ton prosty',N,0) #Switch 0 = plot ; else stem

dft=DFT(N)
Wykres(342,'DFT',dft,1)

inv=InverseDFT(dft)
Wykres(343,'Inverse DFT',inv,0)

spec=spectrum(dft)
spec.pop(0)
Wykres(344,'Spectrum',spec,1)

Wykres(345,'fx = (a * (x * x)) + (b * x) +  c',acords,0)

Wykres(346,'y(t)=2*x(t)^2+12*cos(t)',ycords,0)

Wykres(347,'sin(2pi*7*t)*x(t)-0.2*log10(abs(y(t))+pi)',zcords,0)

Wykres(348,'sqrt(abs(y(t)*y(t)*z(t)))-1.8*sin(0.4*t*z(t)*x(t))',ucords,0)

A=DFT(acords)
AS=spectrum(A)
Wykres(349,'Spectrum',AS,1)

B=DFT(ycords)
BS=spectrum(B)
Wykres([3,4,10],'Spectrum',BS,1)

C=DFT(zcords)
CS=spectrum(C)
Wykres([3,4,11],'Spectrum',CS,1)

D=DFT(ucords)
DS=spectrum(D)
Wykres([3,4,12],'Spectrum',DS,1)

plt.show()
