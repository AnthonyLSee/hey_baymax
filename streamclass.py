
import tweepy
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("text:" + status.text)


    def getID(self,status):
        print(status.id)
