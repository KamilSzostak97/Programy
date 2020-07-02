#Lab 02
#Kamil Szóstak
#sk39454

import numpy as np
import pandas as pd
import scipy.stats as stat
import matplotlib.pyplot as plt

#Manipulowanie danymi

df = pd.DataFrame(
  [['2020-03-01',np.random.normal(),np.random.normal(),np.random.normal()],
  ['2020-03-02',np.random.normal(),np.random.normal(),np.random.normal()],
  ['2020-03-03',np.random.normal(),np.random.normal(),np.random.normal()]],
columns = ['data','A','B','C']
)
#print(df)

#Wybieranie danych z Bazy

df = pd.DataFrame(
  np.random.randint(0,100,size=(20, 3)),
  columns=list('ABC'),
  index=np.arange(1,21)
  )
df.index.names = ['id']
#print(df,'\n\n')
#print(df.head(3),'\n\n')
#print(df.tail(3),'\n\n')
#print(df.index.names,'\n\n')
#print(df.columns,'\n\n')
#print(df.values,'\n\n')
#print(df[2:7],'\n\n')
#print(df.loc[:,'A'],'\n\n')
#print(df.loc[:,['A','B']],'\n\n')
#print(df.iloc[0:2,[0,1]],'\n\n')
#print(df.iloc[5,[0,1,2]],'\n\n')
#print(df.iloc[[0,5,6,7],[0,1]],'\n\n')

#Describe
df = pd.DataFrame(
  np.random.randint(-50,50,size=(20, 3)),
  columns=list('ABC'),
  index=np.arange(1,21)
  )
df.index.names = ['id']
#print(df > 0)
#print(df[df > 0])
#print(df.loc[:, 'A'][df.loc[:, 'A'] > 0])
#print(df.mean(axis = 0))
#print(df.mean(axis = 1))

#Concat
#dfduo = pd.concat((df, pd.DataFrame({'Z' : np.random.randn(20)})))
#print(dfduo)
#print(dfBig.transpose())

#Sortowanie
df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": ['a', 'b', 'a', 'b', 'b']}, index=np.arange(5))
df.index.name = 'id'
#print(df.sort_values(by='id'))
#print()
#print(df.sort_values(by='y', ascending = False))

#Grupowanie
slownik = {'Day': ['Mon', 'Tue', 'Mon', 'Tue', 'Mon'], 'Fruit': ['Apple', 'Apple', 'Banana', 'Banana', 'Apple'], 'Pound': [10, 15, 50, 40, 5], 'Profit':[20, 30, 25, 20, 10]}
df = pd.DataFrame(slownik)
#print(df)
#print(df.groupby('Day').sum())
#print(df.groupby(['Day','Fruit']).sum())

#Wypełnianie danych
df=pd.DataFrame(np.random.randn(20, 3), index=np.arange(20), columns=['A','B','C'])
df.index.name='id'
#print(df)
df['B'] = 1
#print(df)
#calues w kolumnie B zamienione na 1
df.iloc[1,2] = 10
#print(df)
#przypisanie 10 do value w polu [1,2]
df[df < 0] = -df
#print(df)
#Ustawienie ujemnych values na dodatnie

#Uzuepłnianie danych
df.iloc[[0, 3], 1] = np.nan
#print(df)
#dodajamy NaN na wskazane miejsca ( 1 oraz 4 miejsce w kolumnie B)
df.fillna(0, inplace=True)
#print(df)
#zamieniamy poprzednio dodane nany na zera
df.iloc[[0, 3], 1] = np.nan
df=df.replace(to_replace=np.nan, value=-9999)
#print(df)
#zamieniamy poprzednio dodane nany na -9999
df.iloc[[0, 3], 1] = np.nan
#print(pd.isnull(df))
#sprawdza czy value jest = nan jezeli tak to wypisze nam true jezeli nie to false

df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': ['a', 'b', 'a', 'b', 'b']})
#print(df)

#Zadanie 1

#print(df.groupby(['y']).mean())

#Zadanie 2

#print(df['y'].value_counts())

#Zadanie 3

file = pd.read_csv('autos.csv')
#print(file,'\n\n')
#npumpy nie dzialal, pandas wczytal dane bez problemu

#Zadanie 4

#print(file.groupby('make').mean()[['highway-mpg']])

#Zadanie 5

#print(file.groupby('make')['fuel-type'].value_counts())

#Zadanie 6

poly1 = np.polyfit(file['length'], file['city-mpg'], 2)
poly2 = np.polyfit(file['length'], file['city-mpg'], 2)

#print(poly1,'\n\n', poly2)

#Zadanie 7

#print(st.pearsonr(file['length'], file['city-mpg']))

#Zadanie 8

#draw = np.linspace(file['length'].min(), file['length'].max(), 500)
#plt.scatter(file['length'], file['city-mpg'], label = 'Próbki')

#plt.plot(draw, np.polyval(poly1, draw))
#plt.plot(draw, np.polyval(poly2, draw))

#plt.savefig('wykres.png')
#plt.show()

#Zadanie 9

draw = np.linspace(file['length'].min(), file['length'].max(), 500)
gauss = stat.gaussian_kde(file['length'])

plt.figure()
plt.plot(draw, gauss(draw), label = 'Plot')
plt.scatter(file['length'], gauss(file['length']))

#plt.savefig('wykres.png')
#plt.show()

#Zadanie 10

#fig, axs=plt.subplots(2)
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(draw, gauss(draw))
#axs[0].scatter(file['length'], gauss(file['length']))
WykresSzerokosc = np.linspace(file['width'].min(), file['width'].max(), 500)
Gauss = stat.gaussian_kde(file['width'])
#axs[1].plot(WykresSzerokosc, Gauss(WykresSzerokosc))
#axs[1].scatter(file['width'], Gauss(file['width']))
#axs[1].set_title("szerokosc")

#plt.savefig('wykres.png')
#plt.show()

#Zadanie 11

xmin = file['width'].min() ; xmax = file['width'].max()
ymin = file['length'].min() ; ymax = file['length'].max()
xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([xx.ravel(), yy.ravel()])

values = np.vstack([file['width'], file['length']])
kernel = stat.gaussian_kde(values)
f = np.reshape(kernel(positions).T, xx.shape)

fig = plt.figure()
wyk = fig.gca()
wyk.set_xlim(xmin, xmax)
wyk.set_ylim(ymin, ymax)
cfset = wyk.contourf(xx, yy, f, cmap='Blues')
cset = wyk.contour(xx, yy, f, colors='k')
plt.savefig('wykres.png')
plt.savefig('wykres.pdf')
plt.show()
