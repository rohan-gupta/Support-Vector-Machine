import tweepy
import csv, pickle
import datetime
import trim

access_token = "3272774113-OYan4XOEIk3g9leOWhxeROw2my9KirLjMhkQf7c"
access_token_secret = "sN4ipX7MY8AmvqQrzcKJhjW6zsizkoZ7ju7Qw4OS5OBgA"
consumer_key = "tRDsRdePxGbPBvMYCcSswD5Ki"
consumer_secret = "jboSzbE4aaxYH5xyBX7ci88HnwESi2oi0CwYJYBe8F6dJhXngR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTweets(userName):
    alltweets = []
    screen_name = userName

    tweets = api.user_timeline(screen_name=screen_name, count=20)

    id = tweets[-1].id - 1
    alltweets.extend(tweets)

    print("Downloading tweets...")

    for i in range(0, 2):
        tweets = api.user_timeline(screen_name=screen_name, count=20, oldest=id)
        alltweets.extend(tweets)

        print("Downloading tweets...")
        id = tweets[-1].id - 1

    outtweets = []

    for tweet in alltweets:
        if(datetime.datetime.now() - tweet.created_at).days < 1:
            outtweets.append(trim.preprocessTweets(bytes.decode(tweet.text.encode("utf-8"))))

    outtweets = list(set(outtweets))

    print("Tweets Downloaded.\n")
    # Creating csv
    with open('UserData/%s_latest_tweets' % screen_name, 'wb') as f:
        pickle.dump(outtweets, f)