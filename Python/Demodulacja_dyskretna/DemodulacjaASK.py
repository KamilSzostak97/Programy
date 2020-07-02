import math
import array
import numpy as np
import matplotlib.pyplot as plt
from Utilities import Binary,Wykres

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
    Wykres(511,'Sygnal wejsciowy',xcords,ycords)

def ASK(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )*1))
    xcords=np.linspace(0,1,len(ycords))
    Wykres(512,'ASK',xcords,ycords)
    return ycords

def demodulator1(Modulacja,h):
    Demo=[] ; Final=[] ;  Demov2 = []
    sum=0 ; sumabs = 0

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sum = 0
        sum=sum+Modulacja[i]
        Demo.append(sum)

    xcords = np.linspace(0,1,len(Demo))
    Wykres(513,'Demodulacja ASK x(t)',xcords,Demo)

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sumabs = 0
        if (Modulacja[i]>h):
            sumabs=sumabs+(Modulacja[i])
        Demov2.append(sumabs)

    xcords = np.linspace(0,1,len(Demov2))
    Wykres(514,'Demodulacja ASK p(t)',xcords,Demov2)

    for i in range (len(Demov2)):
        roundmt=round(Demov2[i],0)
        if(roundmt==0):
            for x in np.linspace(1/10,2/10):
                Final.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                Final.append(1)

    xcords=np.linspace(0,1,len(Final))
    Wykres(515,'Demodulacja ASK m(t)',xcords,Final)
    return Demo,Demov2,Final

plt.figure()
mt=Binary('Kamil',0)
tb=0.1 ;N=10;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb;A=1;A1=0;A2=1
LIMIT=10
MT(LIMIT)
ycords=ASK(LIMIT)
demodulator1(ycords,0.2)
plt.show()
