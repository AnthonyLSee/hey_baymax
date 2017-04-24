import tweepy, time
from credentials import *
import random

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

database = {"flu":['dizzy', 'dizziness', 'tired', 'sleepy', 'not feeling well',
                'stomache ache', 'stomach pain', 'vomiting', 'puking', 'sore throat',
                    'pain', 'swollen throat', 'fatigue', 'extreme fatigue', 'cold',
                        'diarrhea','fever', 'severe fever', 'stuffy nose', 'watery eyes',
                            'runny nose', 'ear ache', 'stiff neck', 'sneezing',
                                'virus', 'congestion', 'body ache', 'runny nose',
                                'sick', 'coughing', 'cough', 'sneeze', 'sickly',
                                'nausea', 'weak muscle', 'weak muscles', 'lightheaded'],
                "adhd": ['hyperactivity', 'inattention', 'easily distracted'],
                "aids": ['aids', 'hiv', 'sexually active', 'sex'],
                "alzheimers": ['forgetful', 'get lost', 'alzheimers', 'dementia',
                                ],
                "arthritis": ['gout', 'joint', 'joints', 'stiff', 'stiff joints',
                                'swelling', 'redness', 'feet stiff', 'sore muscles',
                                'sore bones'],
                "diabetes": ['blood pressure', 'diabetic',
                                'overweight', 'fat', 'pee often', 'numbness'],
                "cancer": ['cancer', 'lung cancer', 'skin cancer'],
                "asthma": ['shortness of breath', 'wheezing', 'chest pain',
                            'chest pressure', 'inflamed throat'],
                "rabies": ['bit', 'bitten' 'bite'],
                "taken drugs": ['overdose', 'weed', 'crack', 'meth', 'high',
                                    'took drugs', 'drugs'],
                "taken alcohol": ['wine', 'liquor', 'drunk', 'tipsy']
                                }
database_url = {"flu": "https://goo.gl/Ab6vRn",
                    "adhd" : "https://goo.gl/LQ7CwJ",
                        "aids": "https://goo.gl/6YeXBh",
                            "alzheimers": "https://goo.gl/0wV6s3",
                                "arthritis": "https://goo.gl/VIFTW2",
                                    "diabetes": "https://goo.gl/0IoOsC",
                                        "cancer": "https://goo.gl/QXWuz7",
                                            "asthma": "https://goo.gl/ILIj6t",
                                                "rabies": "https://goo.gl/9z91ID",
                                            "taken drugs": "https://goo.gl/LF6L7B",
                                        "taken alcohol": "https://goo.gl/xVXxKu"}

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

    fullResponse = ""
    pos_greeting = ["Hello" , "Hey", "Hi"]
    pos_resp = ["your symptoms show"," signs suggest","there's a possibility"]

    random.shuffle(pos_greeting)
    random.shuffle(pos_resp)

    fullResponse = "{} @{} {} that you may have {}. Here's a link for more info {}".format(
        pos_greeting[0], user, pos_resp[0], disease, database_url.get(disease))

    return fullResponse

def formatError(user):
    fullResponse = ""
    err_greeting = ["Hello","Hey", "Hi"]
    err_resp01 = ["cannot", "can't", "could not", "didn't", "did not"]
    err_resp02 = ["issue", "problem", "illness"]
    err_punct = [".", "..", "!", "!!"]
    stringSets = [err_greeting, err_resp01, err_resp02, err_punct]
    for set in stringSets:
        random.shuffle(set)
    fullResponse = "{} @{} I {} find a possible {} with the symptom(s) you provided{}".format(
        err_greeting[0], user, err_resp01[0], err_resp02[0], err_punct[0]
    )
    return fullResponse

class MyStreamListener(tweepy.StreamListener):

    def respondBack(self,user, status, disease): # corrected

        bodyText = status.replace("@hey_baymax ","")
        print(bodyText) # corrected
        time.sleep(2)

        print("\nResponse Queueing\n")
        time.sleep(2)

        if disease in database:
            sendString = formatPossibility(user,disease)
            api.update_status(sendString)
            print "First Response Sent.\n"

        else:
            sendString = formatError(user)
            api.update_status(sendString)
            print "Second Response Sent.\n"

    def on_status(self, status):
        print("Mention Recieved\n")
        userObj = status.user
        # print(status.location) #location of Status Update
        print(status.created_at) # status date in UCT
        print(userObj.screen_name)
        userScreen_name = str(userObj.screen_name)
        textbody = status.text
        disease = findDisease(textbody,database)
        print(disease)
        self.respondBack(userScreen_name, textbody,disease)
        disease = ""
        textbody = ""
