<h1>Emotion Recognition From Audio Signal</h1>
This is a set of soultions of Emotion Recognition From Audio Signal from Surrey Audio-Visual Expressed Emotion (SAVEE) Database using OpenSmile, Principal Components Analysis and set of classifiers from Scikit-learn library.

The SAVEE database was recorded from four native English male speakers (identified as DC, JE, JK, KL), postgraduate students and researchers at the University of Surrey.The database consists of recordings in 7 different emotions, 480 British English utterances in total.

OpenSmile is used to extract features from .wav file, it generate 1582 feature. After that, I applied PCA (Principal Components Analysis) for dimentionality reduction. Finally, I used different algorithms for classification.

<h3>The different emotions are:</h3>
	
	Anger
	Disgust
	Fear
	Happiness
	Sadness
	Surprise
	Neutral

<h2>Results</h2>
<table>
	<tr> <th>Algorithm</th> <th>Model Performance</th> </tr>
	<tr> <td>Multi Layer Perceptron Classifier</td> <td>80.20%</td> </tr>
	<tr> <td>Logistic Regression + lbfgs Solver</td> <td>76.04%</td> </tr>
	<tr> <td>Linear Discriminant Analysis</td> <td>76.04%</td> </tr>
	<tr> <td>Support Vector Classifier</td> <td> 75%</td> </tr>
	<tr> <td>Logistic Regression</td> <td>75%</td> </tr>
	<tr> <td>K-Neighbors Classifier</td> <td>66.66%</td> </tr>
	<tr> <td>Gaussian Naive Bayes</td> <td>64.58%</td> </tr>
	<tr> <td>Decision Tree Classifier</td> <td>54.16%</td> </tr>
	<tr> <td>Ada Boost Classifier</td> <td>41.66%</td> </tr>
	<tr> <td>Random Forest Classifier</td> <td>32.29%</td> </tr>
	<tr> <td>Discriminant Analysis</td> <td>28.12%</td> </tr>
	<tr> <td>Gaussian Process Classifier</td> <td>17.70%</td> </tr>
</table>

<h2>Requirements</h2>
Python 2.7 and up

<h2>Installation</h2>
The followoing are the prerequiste Python modules that needs to be installed to execute main.py:

	sudo pip install pandas 
	sudo pip install -U scikit-learn

<h2>Downloads</h2>
Clone the repository using the below mentioned command and execute the Python program.
	
	git clone https://github.com/Sehaba95/Emotions-recognition-from-audio-signal.git
	cd Emotions-recognition-from-audio-signal/Classifiers
	python MLPClassifier.py

<h2>Authors</h2>

[Sehaba Amine](https://github.com/Sehaba95)
