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

def ZPT(mt, t, f, tb, koniec):
    ycords=[] ; x = []
    for i in range(len(t)):
        if(mt[i]==0):
          if i + 1 < len(t):
            cords_sin = np.linspace(t[i], t[i+1])
            for m in cords_sin:
              tb=t[i]+5
              ampl = 2*np.pi/ ((t[i+1]-t[i])*0.5 )
              ycords.append(np.sin(ampl*(m  - 1/len(t))+3.14))
          else:
            cords_sin = np.linspace(t[i], koniec)
            for m in cords_sin:
              ycords.append(np.sin(ampl*(m  - 1/len(t))+3.14))
        else:
          if i + 1 < len(t):
            cords_sin = np.linspace(t[i], t[i+1])
            for m in cords_sin:
              tb=t[i]+5
              ampl = 2*np.pi/ ((t[i+1]-t[i])*0.5 )
              ycords.append(np.sin(ampl*(m  - 1/len(t))))
          else:
            cords_sin = np.linspace(t[i], koniec)
            for m in cords_sin:
              ycords.append(np.sin(ampl*(m  - 1/len(t))))
        ycords.append(0)
    x=np.linspace(0,1,len(ycords))
    Wykres(512,'PSK',x,ycords)
    return(ycords)

def demodulator(Modulacja,h):
    Demo=[] ; Final=[] ;  Demov2 = []
    sum=0 ; sumabs = 0

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sum = 0
        sum=sum+Modulacja[i]
        Demo.append(sum)

    xcords = np.linspace(0,1,len(Demo))
    Wykres(513,'Demodulacja PSK x(t)',xcords,Demo)

    for j in range(len(mt)):
        if(mt[j]==0):
            for i in range (len(Modulacja)):
                if(Modulacja[i]<0):
                    sumabs=sumabs+Modulacja[i]
                    Demov2.append(sumabs)
        else:
            for i in range (len(Modulacja)):
                if(Modulacja[i]>0):
                    sumabs=sumabs+Modulacja[i]
                    Demov2.append(sumabs)
        sumabs=0

    xcords = np.linspace(0,0.1,len(Demov2))
    Wykres(514,'Demodulacja PSK p(t)',xcords,Demov2)

    for i in range (len(Demov2)):
        roundmt=round(Demov2[i],0)
        if(roundmt<=0):
            for x in np.linspace(1/10,2/10):
                Final.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                Final.append(1)

    xcords=np.linspace(0,1,len(Final))
    Wykres(515,'Demodulacja PSK m(t)',xcords,Final)

plt.figure()
mt=Binary('AB',0)
mt=[0,1,1,0,1,0]
x=np.linspace(0, 1, len(mt), endpoint=False)
tb=0.1 ;N=10;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb;A=1;A1=0;A2=1
LIMIT=10
MT(len(mt))
ycords=ZPT(mt, x, f, tb, 1)
demodulator(ycords,0.2)
plt.show()
