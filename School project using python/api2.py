import tweepy
import webbrowser
from time import sleep
import json



FollowerMode = True

idsdict = { 'CNN Breaking': 428333,
            'CNN': 759251,
            'Fox News': 1367531 }

  #I have this code here because if I want to sort through the tweets unfiltered I need to search for multiple keywords. This is because twitter only allows speciic enterpireses access.           
search = ['.','a','@','\'','this','to',':(','?','!','$',
           'h','+','_','-','#','b','you', 'c',',','the',
           'i','/','lol','at','this','need','and','RT',
           'if','1', 'd','e','f','g']


consumer_key = 'Yr2w21j6wiZULiuAQAc6BsDJk'
consumer_secret = 'eR3J2aYWn8vzvA3huuwZH17L97OKEHQYmWcxLWctPyHJAZUMV5'
access_token = '1308024341414715392-z5PKvllXZbBZpFy3ecwuwMDhrLPzoi'
access_token_secret = 'cNLynos7esdQSwsLJBUMbT9dCZqlmzDJFST6JHTEcRG1X'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print('Finding tweets...\n')

if FollowerMode == True:
    ids = [str(i) for i in list(idsdict.values())]

class MyStreamListener(tweepy.StreamListener):
    global ids
    global FollowerMode
    tweets = 0
            

            
           
# Define the listener
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)


if FollowerMode == True:
    stream.filter(follow=ids)
else:
    stream.filter(languages=["en"], track = search )