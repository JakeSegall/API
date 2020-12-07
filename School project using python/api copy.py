import tweepy
import webbrowser
import time
consumer_key = "Yr2w21j6wiZULiuAQAc6BsDJk"
consumer_secret = "eR3J2aYWn8vzvA3huuwZH17L97OKEHQYmWcxLWctPyHJAZUMV5"

callback_uri = 'oob' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()

webbrowser.open(redirect_url)

user_pint_input = input("What's the pin value? ")

auth.get_access_token(user_pint_input)

api = tweepy.API(auth)

me = api.me()

# print(me.screen_name, me.id)
listener_list = {}

user_list = [ "jake14886732", "CNN", "FoxNews", "globalnewsto" ]

class MyStreamListener(tweepy.StreamListener):
    this_user_id = ""
    def on_status(self, status):
        if status.user.id_str != self.this_user_id:
            return
        print(status.text)
           

# MyStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener)
# myStream.filter(follow=[str(me.id)])

account_index = 0
for twitter_name in user_list: 
    
    #try-catch exception to catch errors. 
    try:    
        tweets = api.user_timeline(screen_name=twitter_name,
        count=1
        )

        # for info in tweets[:4]:
        #     print("ID: {}".format(info.id))
        #     print(info.created_at)
        #     print(info.text)
        #     print("\n")
        # print(tweets[0].user.id)
        listener_list[account_index] = {}
        listener_list[account_index]["listener"]= MyStreamListener()
        listener_list[account_index]["listener"].this_user_id = str(tweets[0].user.id)
        listener_list[account_index]["Stream"]= tweepy.Stream(auth = api.auth, listener=listener_list[account_index]["listener"])
        listener_list[account_index]["Stream"].filter(track=[str(tweets[0].user.id)], async = True)
        account_index += 1 
    except  tweepy.TweepError as e:
        print("failed to get user timeline, exception thrown", )


        
 



#stream listener



while True: 
    pass