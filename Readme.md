<h1>Emotion Recognition From Audio Signal</h1>
This is my solution of Emotion Recognition From Audio Signal from Surrey Audio-Visual Expressed Emotion (SAVEE) Database using OpenSmile, Principal Components Analysis and K-Nearest Neighbors.

The SAVEE database was recorded from four native English male speakers (identified as DC, JE, JK, KL), postgraduate students and researchers at the University of Surrey.The database consists of recordings in 7 different emotions, 480 British English utterances in total.

OpenSmile is used to extract features from .wav file, it generate 1582 feature. After that, I applied PCA (Principal Components Analysis) for dimentionality reduction. Finally, I used KNN (K-Nearest Neighbors) for classification.

<h3>The different emotions are:</h3>
	
	Anger
	Disgust
	Fear
	Happiness
	Sadness
	Surprise
	Neutral

<h2>Authors</h2>

	Sehaba Amine

<h2>Installation</h2>
The followoing are the prerequiste Python modules that needs to be installed to execute main.py:

	sudo pip install pandas 
	sudo pip install -U scikit-learn


<h2>Requirements</h2>
Python 2.7 and up

<h2>Downloads</h2>
Clone the repository using the below mentioned command and execute the Python program.
	
	git clone https://github.com/Sehaba95/Emotions-recognition-from-audio-signal.git
	cd Emotions-recognition-from-audio-signal
	python main.py


<h2>Contributing</h2>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.