<<<<<<< Updated upstream


import tweepy, time
=======
import tweepy, time, json
>>>>>>> Stashed changes
from credentials import *
from console import console
from streamclass import *


<<<<<<< Updated upstream
import tweetlist as bq


=======
override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener())
myStream.filter(track=['python'])

#onsole.log("Baymax has started\n")
#console.log(api.on_status)
#print(api.on_status)
# print(api.me())
#m = api.me()
#a = m.to_json("test.json")
#print("Baymax has stopped")
>>>>>>> Stashed changes

#for diagnose in ct:
# def talking():
#    for line in bq.tweetlist:
#        api.update_status(line)
#        print(line)
#        print "..."
#        time.sleep(40)
# talking()


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

