import matplotlib.pyplot as plot
from sklearn import svm
import pickle

emotions = ['anger','anticipation','disgust','fear','joy','sad','surprise','trust']

def svmImplementation(userName):
    with open('training_vectors', 'rb') as f:
        emotion_vector = pickle.load(f)

    with open('training_tweets', 'rb') as f:
        temp = pickle.load(f)
        target_classes = []

        for i in range(0,len(temp)):
            target_classes.append(temp[i][0])

    classifier = svm.SVC(C=1, kernel='linear')
    classifier.fit(emotion_vector,target_classes)

    f = open('UserData/%s_latest_tweets' %userName, 'rb')
    tweets = pickle.load(f)
    f.close()

    f = open('UserData/%s_test_vectors' %userName, 'rb')
    vectors = pickle.load(f)
    f.close()

    for i in range(0,len(tweets)):
        print('Tweet: ', tweets[i])
        print('Vectors: ', vectors[i])
        print('Emotion: ', classifier.predict([vectors[i]]))
        print('\n')

