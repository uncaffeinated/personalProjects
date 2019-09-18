# =============================================================================
# A program for use in the Child Language Intervention Lab
# =============================================================================
print("This program only uses CSV files.")
print("""You will have needed to split the text into C units already
using the first two columns after the text in order for this
to work.""")
print("Please remove any and all commas from the associated text, then export the sheet as CSV.")

input("Press enter to continue.")

fileName = input("Please input the file name, including the file extension .csv: ")
fileobj = open(fileName, "r", encoding = 'utf-8')

#Reads the header of the CSV file, in order to separate the columns.
firstLine = fileobj.readline()
firstLine = firstLine.split(",")
print(firstLine)
relIdx = firstLine.index("Reliability")
myIdx = firstLine.index("My Transcript")
agrIdx = firstLine.index("Segmentation_A")
wordsLineA = firstLine.index("# Words/line_A")
wordsLineD = firstLine.index("# Words/line_D")

wordCountA = []
wordCountD = []


for line in fileobj:
    # Sanitzing each line for analysis.
    # TODO: figure out the correct regex needed to clean this up more efficiently
    line = line.lower()
    line = line.replace("xx", "")
    line = line.replace("**", "")
    line = line.replace("<>", "")
    line = line.replace("  ", " ")
    line = line.replace("  ", " ")   
    
    # Splitting the reliability transcript from your own, cleaning up additional data.
    line = line.split(",")
    line[3:] = []
    
    
    # Splits up the reliability into words, and then removes speaker designator
    relSplit = line[0].split(" ")
    del relSplit[0]  
    
    # Splits up your transcript into words, and then removes speaker designator
    mySplit = line[1].split(" ")
    del mySplit[0]

    # If the C-units match according to the preliminary works that you did, count the # of words.
    if line[agrIdx] == "1":
        a = min(len(relSplit), len(mySplit))
        d = max(len(relSplit), len(mySplit)) - a
        wordCountA.append(a)
        wordCountD.append(d)
    # Else, just return 0
    else:
        wordCountA.append(0)
        wordCountD.append(0)

input("Press enter to get the number of words that agree in each line.")
for i in range(len(wordCountA)):
    print(wordCountA[i])
input("You can copy and paste the above into the appropriate Excel column.")

input("Once you are done copying and pasting these numbers, press enter to get the number of words that disagree.")
for i in range(len(wordCountA)):
    print(wordCountD[i])
input("After you are done copying these numbers into the appropriate column, you can move on to your next task.")
