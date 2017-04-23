
import tweepy, time
import tweetlist as bq
# from catcher import *
from credentials import *
from console import console
from streamclass import *

def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    console.log("\n\nBaymax Bot is Running...\n")

    while(True):
        myStream.filter(track=['@hey_baymax'])

def respondBack(api,user):
    api.update_status("Hello {}!".format(user))

if __name__ == "__main__":
    main()
