
import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("text:" + status.text)


    def getID(self,status):
        print(status.id)
