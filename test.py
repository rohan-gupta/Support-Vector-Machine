import pickle

file = open('UserData/rohan_gupta96_latest_tweets', 'rb')
data = pickle.load(file)

print(data)
