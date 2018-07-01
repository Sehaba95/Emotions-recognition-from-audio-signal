#!/usr/bin/env python 

import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load DATA 
df = pd.read_csv('dataset.csv')

# Header for Features without Labels 
features = [str(i) for i in range(1,1583)]

# Standarize the DATA 
X = df.loc[:,features].values

Y = df.loc[:,'label'].values

X = StandardScaler().fit_transform(X)

# PCA  
# n : Number of principal components 
n = 90
pca = PCA(n_components = n)

X = pca.fit_transform(X)

#Split data to train and test 
X_train, X_test, Y_train, Y_test = train_test_split (X,Y,test_size=0.2)

#Create a Ada Boost Classifier instance 
classifier = AdaBoostClassifier()

#Fit the classifier
classifier.fit(X_train,Y_train)

#Calculate the score (Accuracy)
score = classifier.score(X_test,Y_test)

#Printing the score
print(score)