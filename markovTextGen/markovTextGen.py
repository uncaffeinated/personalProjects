import markovify
import nltk
import re

# =============================================================================
# See Markovify README
# =============================================================================

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# =============================================================================
# Defining important functions; grabbing files
# =============================================================================
        
def getFileName():		
	tryText = True
	while tryText == True:
		try:
			old = input("Please provide the name of the file you want to create sentences from. (eg. file.txt) ")
			if old.endswith(".txt"):
				with open(old) as f:
					text = f.read()
				tryText = False
			else:
				print("Please provide a valid file name. (Try including .txt)")
		except:
			print("Please provide a valid file name. (Try including .txt)")
	return text

def getNewText():
	tryNewText = True
	while tryNewText == True:
		try: 
			new = input("Please provide the name of the file you want to write sentences to. (eg. newFile.txt) ")
			if new.endswith(".txt"):
				tryNewText = False
			else:
				print("Please provide a valid file name. (Try including .txt)")
		except:
			print("Please provide a valid file name. (Try including .txt)")
	return new

def howMany():
    tryInput = True
    while tryInput == True:
        try:
            num = int(input("How many sentences would you like to try to generate? "))
            tryInput = False
        except:
            print("Please input a valid integer.")
    return num
   
text = getFileName()
new = getNewText()

# =============================================================================
# The meat. We begin by opening the file and preparing to append content.
# =============================================================================
tryAgain = True
while tryAgain == True:
    new_stuff = open(new,"a+")
    
    num = howMany()
    
    #Generating a model... (State size refers to the # of words in each markov state)
    text_model = POSifiedText(text, state_size=2)
    for i in range(num):
        new_stuff.write(text_model.make_short_sentence())
        new_stuff.write("\n")
    new_stuff.close()
    
    tryAns = True
    while tryAns == True:
        ans = input("Would you like to continue? Y or N")
        if ans == "Y":
            tryAns = False
        elif ans == "N":
            tryAgain = False
            tryAns = False
    