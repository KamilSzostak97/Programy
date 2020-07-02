from sklearn import datasets
import scipy
import pandas as pd
import numpy as np
from random import seed,random
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from scipy.cluster import hierarchy
from sklearn.cluster import KMeans
from sklearn.metrics import jaccard_score
from sklearn.decomposition import PCA
import scipy.sparse as sparse

def find_perm(clusters, Yreal, Ypred):
    perm=[]
    for i in range(clusters):
        idx = Ypred == i
        new_label = scipy.stats.mode(Yreal[idx])[0][0]
        perm.append(new_label)
    return [perm[label] for label in Ypred]

def newdf(PC,Groups):
    df = pd.DataFrame(Groups , columns = ['target'])

    principalDf = pd.DataFrame(data = PC
                 , columns = ['principal component 1', 'principal component 2'])

    finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

    return finalDf

def plot(finalDf):
    colors = ['r', 'g', 'b', 'y', 'c', 'm']

    for i in range(140):
        plt.scatter(finalDf.loc[i, 'principal component 1'],
                   finalDf.loc[i, 'principal component 2'],
                   c = colors[finalDf.loc[i, 'target']],
                   s = 7)

def compare(compare,Y):
    ax = fig.add_subplot(1, 3, 3, projection='3d')
    for i in range(140):
        if compare.loc[i, 'target'] == Y[i]:
            plt.scatter(compare.loc[i, 'principal component 1'],
                       compare.loc[i, 'principal component 2'],
                       c = 'g',
                       s = 7)
            ax.scatter(compare.loc[i, 'principal component 1'],
                       compare.loc[i, 'principal component 2'],
                       random(), c='g')
        else:
            plt.scatter(compare.loc[i, 'principal component 1'],
                       compare.loc[i, 'principal component 2'],
                       c = 'r',
                       s = 7)
            ax.scatter(compare.loc[i, 'principal component 1'],
                       compare.loc[i, 'principal component 2'],
                       random(), c='r')


iris=datasets.load_iris()
X=iris.data
Y=iris.target
#print(X)
#print(Y)
Close = AgglomerativeClustering(3,linkage='single').fit(X)
Medium = AgglomerativeClustering(3,linkage='average').fit(X)
Far = AgglomerativeClustering(3,linkage='complete').fit(X)
Ward = AgglomerativeClustering(3,linkage='ward').fit(X)
#print(Close.labels_)
#print(Medium.labels_)
#print(Far.labels_)
#print(Ward.labels_)

clusters=3
Yreal = Y
Just = AgglomerativeClustering(3).fit(X)
Ypred = Just.labels_

Yn=find_perm(3,Y,Just.labels_)
Ynew=np.asarray(Yn)

perm = find_perm(clusters,Yreal, Ypred)
Before=jaccard_score(Yreal, Ypred,average='macro')
After=jaccard_score(Yreal, perm,average='macro')
#print(Before,After)

Xzapas=X
pca = PCA(n_components=2)
PC = pca.fit_transform(Xzapas)

First=newdf(PC,Close.labels_)
Second=newdf(PC,Medium.labels_)
Third=newdf(PC,Far.labels_)
Fourth=newdf(PC,Ward.labels_)
Fifth=newdf(PC,perm)
Test=newdf(PC,Y)
kmeans = KMeans(3).fit(X)
kmeans = newdf(PC,kmeans.labels_)
gmm = GaussianMixture(n_components=3).fit(X)
gmm = newdf(PC,gmm.predict(X))
plt.figure()
plt.subplot(231)
plot(First)
plt.subplot(232)
plot(Second)
plt.subplot(233)
plot(Third)
plt.subplot(234)
plot(Fourth)
plt.subplot(235)
plot(kmeans)
plt.subplot(236)
plot(gmm)

seed(1)
z=[]
for i in range(len(PC)):
	value = random()
	z.append(value)
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 3, 1, projection='3d')
plt.figure()
plt.subplot(1, 3, 1)
for i in range(3):
    points = PC[i == Y]
    hull = scipy.spatial.ConvexHull(points)
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.scatter(PC[:, 0], PC[:, 1], c=Y , s = 7)
ax.scatter(PC[:, 0], PC[:, 1], z, c=Y)

plt.subplot(1, 3, 2)
for i in range(3):
    points = PC[i == Ynew]
    hull = scipy.spatial.ConvexHull(points)
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.scatter(PC[:, 0], PC[:, 1], c=Ynew , s = 7)
ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.scatter(PC[:, 0], PC[:, 1], z, c=Ynew)

plt.subplot(1, 3, 3)
#compare(Test,Y)
#compare(First,Y)
#compare(Second,Y)
#compare(Third,Y)
#compare(Fourth,Y)
compare(Fifth,Y)
#plt.show()

Z = hierarchy.linkage(PC, 'single')
plt.figure()
dn = hierarchy.dendrogram(Z)
hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
plt.show()
