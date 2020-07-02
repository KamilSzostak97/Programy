
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from Utilities import Binary,wartoscProgowa,Wykres

def FSK():
    FSK=[]
    for i,j in zip(TBs,t):
        if i == 1:
            FSK.append(A1 * np.sin(2 * np.pi *f*j + fi))
        if i==0:
             FSK.append(A1 * np.sin(2 * np.pi *f1*j + fi))
    return FSK

def demo():
    DemoX1=[] ; DemoX2=[]
    for i,j in zip(FSK,t):
        DemoX1.append(i* A1 * np.sin(2 * np.pi *f1*j + fi))

    for i,j in zip(FSK,t):
        DemoX2.append(i* A1 * np.sin(2 * np.pi *f2*j + fi))

    pt1 = [];pt2 = [];pt = []
    for i in range(z1):
        x0 = 0 ; x1 = 0
        for j in range(50):
            x0 = x0 + DemoX1[(i * 50) + j]
            x1 = x1 + DemoX2[(i * 50) + j]
        pt1.append(x0) ; pt2.append(x1)
        pt.append(x0 - x1)

    interpolatingFSK=interp1d(x, pt, kind='previous')
    FSK_pt=interpolatingFSK(t)
    return DemoX1,DemoX2,FSK_pt

mt=Binary('Kamil',0)
plt.figure()
fi0=0 ; fi1=np.pi;fi = np.pi;A1=1;A2=0.3;Tb=1 ;N=1/Tb;f = N * (Tb ** -1)
f1 = (N + 1)/Tb;f2 = (N + 2)/Tb;x=50;z1=len(mt);prb=x*(z1/Tb);prb1=int(prb)
t = np.linspace(0,z1,prb1);x = np.linspace(0,z1,z1);h=10

interpolacja = interp1d(x, mt, kind='previous')
TBs = interpolacja(t)
Wykres(511,'sygnal wejsciowy',t,TBs)
FSK=FSK()
Wykres(512,'FSK',t,FSK)
[DemoX1,DemoX2,FSK_pt]=demo()
FSKwp=wartoscProgowa(FSK_pt,h)
Wykres(513,'Demodulacja FSK x1(t)',t,DemoX1)
Wykres(514,'Demodulacja FSK x2(t)',t,DemoX2)
Wykres(515,'Demodulacja FSK p(t)',t,FSKwp)

plt.show()
