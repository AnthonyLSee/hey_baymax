import tweepy, time
from catcher import *
from credentials import *
import random

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

database = {"flu":['dizzy', 'dizziness', 'tired', 'sleepy', 'not feeling well',
                'stomache ache', 'stomach pain', 'vomiting', 'puking', 'sore throat',
                    'pain', 'swollen throat', 'fatigue', 'extreme fatigue', 'cold',
                        'diarrhea','fever', 'high fever', 'stuffy nose', 'watery eyes',
                            'runny nose', 'ear ache', 'stiff neck', 'sneezying',
                                'virus', 'congestion'],
                "adhd": ['hyperactivity', 'inattention', 'easily distracted'],
                "aids": ['aids', 'hiv'],
                "alzheimers": ['forgetful', 'get lost'],
                "arthritis": ['gout', 'joint', 'joints', 'stiff', 'stiff joints',
                                'swelling', 'redness']
                                }
database_url = {"flu": "https://goo.gl/Ab6vRn",
                    "adhd" : "https://goo.gl/LQ7CwJ",
                        "aids": "https://goo.gl/6YeXBh",
                            "alzheimers": "https://goo.gl/0wV6s3",
                                "arthritis": "https://goo.gl/VIFTW2"}

def findDisease(text, dic):
   # Bigger the counter --> more symptoms --> higher possibliy that its x disease

    listofText = text.split()                   # str -> list
    bigList = []                                # bigList will hold all the holders
    holder = []                                 # holder will hold disease and symptom counter
    symptomsCounter = 0                         # How many symptoms there are

    for disease in dic:                         # Iterate through the disease database
        currentDiseaseSymp = dic.get(disease)   # Grab the symptoms
        holder.append(disease)                  # Add disease to holder
        for currentString in listofText:        # Iterate through the body of text
            if currentString in currentDiseaseSymp:  # If word is a symptom
                symptomsCounter += 1            # Iterate counter
        holder.append(symptomsCounter)          # Save the counter
        bigList.append(holder)                  # Save the holder
        holder = []                             # Reset the holder
        symptomsCounter = 0                     # Reset the counter

    highestProb = [0,0]                   # Some default
    for disease in bigList:
        if disease[1] > highestProb[1]:         # If counter > current highest counter
            highestProb = disease               # Swap

    if highestProb[0] == 0:
        highestProb[0] = "N/A"
    return highestProb[0]                       # Return disease

def formatPossibility(user,disease):
    wholeString = ""
    stringSetOne = ["Hello","Hey"]
    stringSetTwo = ["your symptoms show","I believe","there's a possibility"]
    random.shuffle(stringSetOne)
    random.shuffle(stringSetTwo)

    wholeString = "{} @{} , {} that you could have {}. Here's a link for more info {}".format(
        stringSetOne[0],user,stringSetTwo[0],disease,database_url.get(disease))
    return wholeString


def formatError(user):
    wholeString = ""
    stringSetOne = ["Hello","Hey"]
    stringSetTwo = ["cannot","can't","did not"]
    stringSetThree = ["issue","problem","illness"]
    stringSetFour = ["!","!!","!!!"]
    stringSets = [stringSetOne,stringSetTwo,stringSetThree,stringSetFour]
    for set in stringSets:
        random.shuffle(set)
    wholeString = "{} @{} I {} find a possible {} with the symptoms you provided{}".format(
        stringSetOne[0],user,stringSetTwo[0],stringSetThree[0],stringSetFour[0]
    )
    return wholeString


class MyStreamListener(tweepy.StreamListener):

    def respondBack(self,user, status, disease): # corrected
        greetings = ["Hey","Yo!","Whats up","Hello"]
        end1 = ["!","!!","!!!","!!!!"]
        end2 = [" bleep"," bloop"," skeet"," skert"]

        bodyText = status.replace("@hey_baymax ","")
        print(bodyText) # corrected
        time.sleep(4)
        random.shuffle(greetings)
        random.shuffle(end1)
        random.shuffle(end2)

        print("Response Queueing\n") #our error checking
        time.sleep(4)

        if disease in database:
            sendString = formatPossibility(user,disease)
            api.update_status(sendString)
            # Still need to parise status
            # Use api.update_status
            #api.update_status("Hello @{} ,I think you could have {}!".format(user,disease))
            #print "Phase 2"
            #time.sleep(5) # Time Delay in Reply
            #api.update_status("Here @{} , read more here {}".format(user,)) #create webMD style links
            #print("Hey @{} " + " I think you may have the flu!", user)
            print "First Response Sent.\n"
        else:
            sendString = formatError(user)
            api.update_status(sendString)
            #api.update_status("{} @{} {}{}".format(greetings[0],user,end1[0],end2[0]))
            print "Second Response Sent.\n"

    def on_status(self, status):
        print("Mention Recieved\n")
        userObj = status.user
        print(userObj.screen_name)
        userScreen_name = str(userObj.screen_name)
        textbody = status.text
        disease = findDisease(textbody,database)
        print(disease)
        self.respondBack(userScreen_name, textbody,disease)
        disease = ""
        textbody = ""
