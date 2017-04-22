import tweepy, time
from credentials import *
from console import console

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


console.log("Baymax has started\n")

print("...")
#for diagnose in ct:
# def talking():
#    for line in baymax_quotes.tweetlist:
#        api.update_status(line)
#        print(line)
#        print "..."
#        time.sleep(40)
# talking()
