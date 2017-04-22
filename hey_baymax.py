
import tweepy, time
import tweetlist as bq
from credentials import *
from console import console
from streamclass import *


def respondBack(api,user):      # tweepy Obj and username
    api.update_status("Hello {}!".format(user))


def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    console.log("Baymax has started!\n")

    while(True):
        myStream.filter(track=['@hey_baymax'])
    #
    # mentions = api.mentions_timeline(count=1)
    #
    # for mention in mentions:
    #     print(mention.text)
    #     print(mention.user.screen_name)

    # while(True):
    #     pass
    #
    #     # If got message, use respondBack

if __name__ == "__main__":
    main()
