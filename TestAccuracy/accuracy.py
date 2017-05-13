from bs4 import BeautifulSoup
import re
import itertools
import pickle

# file = open('training_tweets', 'rb')
# data = pickle.load(file)
#
# print("Size of corpus:",len(data))
#
# partition1 = 9273
# partition2 = 4637
#
# train = []
# test = []
#
# # training data
# for i in range(0,partition1):
#     train.append(data[i])
# # test data
# for i in range(partition1, partition1+partition2):
#     test.append(data[i])
#
# print("Size of train corpus",len(train))
# print("Size of test corpus", len(test))
#
# file1 = open('train_accuracy', 'wb')
# file2 = open('test_accuracy', 'wb')
#
# pickle.dump(train,file1)
# pickle.dump(test,file2)

file = open('train_accuracy', 'rb')
data = pickle.load(file)

for i in range(0,100):
    print(data[i])