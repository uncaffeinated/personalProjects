# =============================================================================
# A fortune telling bot.
# =============================================================================
import tweepy
import markovify
import nltk
import re
import time

#Adding an additonal NLP library to make tweets more grammatically correct
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

#Connecting to Twitter. 
consumer_key = "ZPaFv2tsEPwnwR8jzABbNxRYr"
consumer_secret = "KLWMib19o8XrTOItKhceQHyGFkN4CguhM7z2gLkQxxLNKMeOUN"

access_key = "1096539403734974464-VpAXQhj8sbIsqKMgifgnQ24j5nurEW"
access_secret = "5Bg5HCOJUlDmcl2E5sn5TBLrkHWMqNkCmrgesgu9D9GG5"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')
       
api = tweepy.API(auth)

#Follows everyone that follows Zostra
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    
# =============================================================================
# Markovifying all of the source text.
# =============================================================================
originalFortunes = 'fortunes.txt'

#Opening originalFortunes for the generation of the probability matrix
with open(originalFortunes) as f:
    text = f.read()

#Generating the probability matrix.
text_model = POSifiedText(text, state_size=2)

#Keep trying to make sentences until a valid one is made.
while True:
    tryAgain = True
    while tryAgain:
        newSentence = str(text_model.make_short_sentence(140))
        if newSentence == "None":
            print("An error has occured. Trying again.")
        else:
            tryAgain = False

# ============================================================================= 
# #Attempting to post something to Twitter.
# =============================================================================
    print(newSentence)
    try:
        api.update_status(status=newSentence)
        print("Done.")
    except:
        print("Something went wrong.")
    #Sets the time between tweets in seconds. 1800 = 30 minutes. 3600 = 1 hour.
    time.sleep(3600)

