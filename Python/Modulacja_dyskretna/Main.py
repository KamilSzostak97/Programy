import math
import array
import numpy as np
import matplotlib.pyplot as plt
from Utilities import Binary,Wykres,Wykres_xlim,Spectrum,bandwidth
import warnings
warnings.filterwarnings("ignore")

def MT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(1)
    xcords=np.linspace(0,1,len(ycords))
    Wykres(421,'Sygnal wejsciowy',xcords,ycords)

def ZAT(LIMIT):
    ycords=[]
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )))
    xcords=np.linspace(0,1,len(ycords))
    Wykres(423,'ZA(t)',xcords,ycords)

    [xcords,spectrum]=Spectrum(ycords)
    Wykres_xlim(424,'Widmo sygnalu',[0,0.17],xcords,spectrum)

    print('Bandwidth of Za(t) is equal to ',bandwidth(ycords))
    #bw 1.1102230246251565e-16

def ZFT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )))
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(80*np.pi*(x  - 1/10 )))
    xcords=np.linspace(0,1,len(ycords))
    Wykres(425,'ZF(t)',xcords,ycords)

    [xcords,spectrum]=Spectrum(ycords)
    Wykres_xlim(426,'Widmo sygnalu',[0,0.24],xcords,spectrum)

    print('Bandwidth of Zf(t) is equal to ',bandwidth(ycords))
    #bw 1.1102230246251565e-16

def ZPT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(20*np.pi*(x  + 0 )))
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(20*np.pi*(x  - np.pi )))
    xcords=np.linspace(0,1,len(ycords))
    Wykres(427,'ZP(t)',xcords,ycords)

    [xcords,spectrum]=Spectrum(ycords)
    Wykres_xlim(428,'Widmo sygnalu',[0,0.1],xcords,spectrum)

    print('Bandwidth of Zp(t) is equal to ',bandwidth(ycords))
    #bw 0.00037399113886860125

plt.figure()
mt=Binary('Kamil',0)
LIMIT=10;tb=0.1
N=2;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb
A=1;A1=0;A2=1

MT(LIMIT)
ZAT(LIMIT)
ZFT(LIMIT)
ZPT(LIMIT)

plt.subplot(422).remove()

plt.show()
