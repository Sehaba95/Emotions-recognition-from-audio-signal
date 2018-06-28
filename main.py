#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 26 00:17:36 2018

@author: Sehaba Amine

Email : sehaba.amine2705@gmail.com

"""

import pandas 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
from sklearn.model_selection import train_test_split

##########################################################################################################################
##################################################Principal Component Analysis############################################
##########################################################################################################################

# Header initialization 
features_labeled = [ str(i) for i in range(0,1584)]

features_labeled[0] = 'Label'

# Load DATA 
df = pandas.read_csv('dataset.csv',names = features_labeled,header=0)

# Header for Features without Labels 
features = [str(i) for i in range(1,1583)]

# Standarize the DATA 
x = df.loc[:,features].values

y = df.loc[:,'Label'].values

#Heterogene -> Homogene 
x = StandardScaler().fit_transform(x)

# PCA Projection 
# n : Number of principal components 

n = 90
pca = PCA(n_components = n)

principalComponents = pca.fit_transform(x)

#Features labels
PC_features = ["PC"+str(i) for i in range(1,n+1)]

#Convert the principal components to Pandas DataFrame
principalDF = pandas.DataFrame(data = principalComponents, columns =PC_features)

#Extract features from data
X = principalDF.loc[:,PC_features].values

#Extract targets from data
y = df.loc[:,'Label'].values

############################################################################################################################
########################################### K NEAREST NEIGHBORS ############################################################
############################################################################################################################
X_train, X_test, Y_train, Y_test = train_test_split (X,y,test_size=0.2)

classifier = neighbors.KNeighborsClassifier(n_neighbors=10)
classifier.fit(X_train,Y_train)
score = classifier.score(X_test, Y_test)

print("Recognition rate: "+str(score))
