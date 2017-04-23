import tweepy
from credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        userObj = status.user
        print(userObj.screen_name)

        #print(api.get_user(userObj.screen_name))

        #id = status.id
        #username = api.get_user(id)
        #print(username)

    #def getID(self,status):
#        print(status.id)
