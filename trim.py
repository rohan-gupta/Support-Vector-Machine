from bs4 import BeautifulSoup
import re
import itertools

def preprocessTweets(tweet):

    # 1 Remove HTML Tags
    soup = BeautifulSoup(tweet, 'html.parser')
    cleaned_tweet = soup.get_text()

    # 2 Remove appostophes
    appostophes= {"'s" : " is", "'re": " are", "'t" : " not", "'d" : " had" , "'m":" am", "'ve":" have"}
    slist = cleaned_tweet.split()
    newsen=[]

    for word in slist:
        for candid in appostophes:
            if candid in word:
                word=word.replace(candid,appostophes[candid])
        newsen.append(word)

    cleaned_tweet=" ".join(newsen)

    # 3 Split attached words
    # ans = ""
    # for a in re.findall('[A-Z][^A-Z]*',cleaned_tweet):
    #     ans += a.strip()+' '
    # cleaned_tweet = ans


    # 4 Conversion of words like luv to love
    # tweet = 'luv'
    # tweet =_slang_loopup(tweet)

    # print(tweet)

    # 5 Standardizing words like i am happpppyyy to i am happy
    temp =''.join(''.join(s)[:2] for _, s in itertools.groupby(cleaned_tweet))
    cleaned_tweet = temp

    #6 Remove URL
    cleaned_tweet= re.sub(r"http\S+", "",cleaned_tweet)

    return cleaned_tweet
