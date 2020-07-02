import numpy as np
import matplotlib.pyplot as plt

def tile(value, count):
    return [value for __ in range(int(count))]

def linspace(low, high, stepCount):
    step = (high - low) / (stepCount - 1)
    values = [low + step * i for i in range(stepCount)]
    return values

def Wykres(Spot,title,xcords,ycords):
    if(isinstance(Spot,list)):
        plt.subplot(Spot[0],Spot[1],Spot[2])
    else:
        plt.subplot(Spot)
    plt.title(title)
    plt.plot(xcords,ycords)
