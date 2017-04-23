import tweepy, time
from catcher import *
from credentials import *
import random

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


catcher_sick1 = ["789", "856", "945", "609", "9001", "1001", "809"] # testing cases
flu_catcher = {"flu":['dizzy', 'dizziness', 'tired', 'sleepy', 'not feeling well',
                'stomache ache', 'stomach pain', 'vomiting', 'puking', 'sore throat',
                    'pain', 'swollen throat', 'fatigue', 'extreme fatigue', 'cold',
                        'diarrhea','fever', 'high fever', 'stuffy nose', 'watery eyes',
                            'runny nose', ]}
flu_response = [] # this will replace catcher_sick1

class MyStreamListener(tweepy.StreamListener):

    def respondBack(self,user, status): # corrected
        sometext = ["Hey","Yo!","Whats up","Hello"]
        sometext2 = ["!","!!","!1!!","!!1!"]
        sometext3 = ["!!","!","1!","!!!"]
        #status = status.text # added

        bodyText = status.replace("@hey_baymax ","")
        print(bodyText) # corrected
        print(type(user))
        time.sleep(2)
        random.shuffle(sometext)
        random.shuffle(sometext2)
        random.shuffle(sometext3)


        print("RespondingNow") #our error checking
        time.sleep(2)

        if bodyText in catcher_sick1: #added
            # Still need to parise status
            # Use api.update_status
            api.update_status("Hey @{} I think you are wierd!".format(user))
            #print("Hey @{} " + " I think you may have the flu!", user)
            print "Sent!"
        else:
            api.update_status("{} @{} {}{}".format(sometext[0],user,sometext2[0],sometext3[0]))
            print "Sent!!"

        #try:
        #    randomlizeList = random.shuffle(self.sometext)
        #    randomSaying = randomlizeList[0]
        #    print("RespondingNow")
        #    api.update_status("{} @{}!".format(randomSaying,user))
        #except:
        #    api.update_status("I dont understand @{}".format(user)) #

    def on_status(self, status):
        print("Got message")
        userObj = status.user
        print(userObj.screen_name)
        userScreen_name = str(userObj.screen_name)
        textbody = status.text
        self.respondBack(userScreen_name, textbody)
