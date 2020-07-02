#Lab01
#Kamil Szóstak
#sk39454

import numpy as np
from numpy.lib.stride_tricks import as_strided

#Tablice
a=np.array([1,2,3,4,5,6,7])
b=np.array([[1,2,3,4,5], [6,7,8,9,10]])
c=np.transpose(b)
#print(np.arange(1,101))
#print(np.linspace(0, 2, num=10))
#print( np.arange(0,101,5) )

#Liczby losowe
#print(np.around(np.random.normal(0, 20, 20), 2))
#print ( np.random.randint(1, 1000, 100) )
#print( np.zeros((3,2)) )
#print( np.ones((3,2)) )
#print ( np.random.randint(1, 1000,(5,5),dtype='int32') )
a=np.linspace(0,10)
b=a.astype(int)

# Selekcja danych
b=np.array([[1,2,3,4,5], [6,7,8,9,10]],dtype=np.int32)
#print(np.ndim(b))
#print(np.size(b))
#print (b[0,1],b[0,3])
#print( b[0,0] )
#print ( b[0,0], b[1,0] )
a=np.random.randint(0, 100,(20,7),dtype='int32')
#for x in range(0, 4):
#    print( a[x,:] )

#Operacje matematyczne i logiczne
a=np.random.randint(0, 10,(3,3),dtype='int32')
b=np.random.randint(0, 10,(3,3),dtype='int32')
#print(a+b)
#print(a*b)
#print(a/b)
#print(a**b)
#print(b**a)
#print(sum(np.diag(b)))

#Dane Statystyczne
s=b.sum()
m=np.min(b)
mx=np.max(b)
StandardDiviation=np.std(b)
#print(s,m,mx,StandardDiviation)
avg=np.average(b,axis=1)
#print(avg)
avg=np.average(b,axis=0)
#print(avg)

#Rzutowanie wymiarów za pomocą shape lub resize
array=np.arange(1,51)
newarray=np.reshape(array,(10,5))
newarraysize=np.resize(array,(10,5))
arrayravel=np.ravel(b)
a=np.random.randint(1, 10,5,dtype='int32')
b=np.random.randint(1, 10,4,dtype='int32')
newa=a[:,np.newaxis]
c=newa+b

#Sortowanie Danych
a=np.random.randn(5,5)
#print(a)
#print()
#a.sort(axis=1)
#print(a)
#print(a)
#print()
#a.sort(axis=0)
#a = a[::-1]
#print(a)
b=np.array([(1,'MZ','mazowieckie'),(2,'ZP','zachodniopomorskie'),(3,'ML','małopolskie')])
newb=np.resize(b,(3,3))
sortedb = b[np.argsort(b[:, 1])]
#print(sortedb)

#Zadanie 1
a=np.random.randint(1,100,(10,5))
b=np.trace(a)
np.diag(a)
#print(b)
#print(np.diag(a))

#Zadanie 2
a=np.random.normal(size=10)
b=np.random.normal(size=10)
c=a*b
#print(c)

#Zadanie 3
a=np.random.randint(1, 101,50,dtype='int32')
b=np.random.randint(1, 101,50,dtype='int32')

rea=np.reshape(a,(10,5))
reb=np.reshape(b,(10,5))

final=rea+reb

#print(final)

#Zadanie 4
a=np.random.randint(1, 101,(4,5),dtype='int32')
b=np.random.randint(1, 101,(5,4),dtype='int32')
rea=np.reshape(a,(5,4))
final=rea+b
#print(final)

#Zadanie 5

mat1=np.random.randint(1, 10,(3,4),dtype='int32')
mat2=np.random.randint(1, 10,(3,4),dtype='int32')
#print(mat1[:,2]*mat2[:,2])
#print(mat1[:,3]*mat2[:,3])

#Zadanie 6
an=np.random.normal(size=(2,3))
bn=np.random.normal(size=(2,3))
avgan=np.average(an)
avgbn=np.average(bn)
stdan=np.std(an)
stdbn=np.std(bn)
van=np.var(an)
vbn=np.var(bn)

au=np.random.uniform(size=(2,3))
bu=np.random.uniform(size=(2,3))
avgau=np.average(au)
avgbu=np.average(bu)
stdau=np.std(au)
stdbu=np.std(bu)
vau=np.var(au)
vbu=np.var(bu)
'''
print('averages\n')
print(avgan)
print(avgbn)
print(avgau)
print(avgbu,'\n')
print('Standard Diviation\n')
print(stdan)
print(stdbn)
print(stdau)
print(stdbu,'\n')
print('Variance\n')
print(van)
print(vbn)
print(vau)
print(vbu)
'''

#Zadanie 7

a=np.random.randint(1, 10,(2,2),dtype='int32')
b=np.random.randint(1, 10,(2,2),dtype='int32')
#print(a,'\n\n',b,'\n\n')
c=a*b
cd=np.dot(a,b)
#print('a*b=\n',c,'\n\n','np.dot(a,b)=\n',cd)

#Zadanie 8

a = np.random.randint(1, 101, [6, 6])
#print(np.lib.stride_tricks.as_strided(a, [3, 5]))

#Zadanie 9

a = np.random.randint(1, 101, [6, 6])
b = np.random.randint(1, 101, [6, 6])

c=np.vstack((a,b))
d=np.hstack((a,b))

#print(a,'\n\n',b)

#Zadanie 10

a = np.arange(0,24)
a=np.reshape(a,(4,6))
print(a.strides)
max1 = np.amax(as_strided(a,(2,3),(24,4)))
max2 = np.amax(as_strided(a+3,(2,3),(24,4)))
max3 = np.amax(as_strided(a+12,(2,3),(24,4)))
max4 = np.amax(as_strided(a+15,(2,3),(24,4)))
#print(max1,max2,max3,max4)
