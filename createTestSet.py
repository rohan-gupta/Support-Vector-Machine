import csv
import pickle
from nltk.tokenize import word_tokenize as w

emotions = ['anger','anticipation','disgust','fear','joy','sad','surprise','trust']

def createTestSet(userName):
    print('Creating test vector set')

    file = open('UserData/%s_latest_tweets' %userName, 'rb')
    tweets = pickle.load(file)

    data = []

    for i in range(0,len(tweets)):
        tweet = tweets[i]
        tweet = tweet.lower()
        text = w(tweet)

        vector = [0, 0, 0, 0, 0, 0, 0, 0]
        index = -1

        for emotion in emotions:
            file = open('EmotionLexicons/%s.txt' % emotion, 'r')
            vocab = file.read().split()

            index += 1

            for word in text:
                if word in vocab:
                    vector[index] += 1

        data.append(vector)

    file = open('UserData/%s_test_vectors' % userName, 'wb')
    pickle.dump(data, file)
    print('Created test vector set\n')

