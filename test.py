import sys, io, os
from sys import argv

print("Question 1")
# Question 1
def reverseString(inputString):
    print(inputString[::-1])
    return inputString[::-1]
x = reverseString("dog")
print("Question 2")
# Question 2
def revereStringOrder(inputWords):
    wordsList = inputWords.split()
    wordsList.reverse()
    wordsList = " ".join(wordsList)
    print(wordsList)
    return wordsList
y = revereStringOrder("the machines are coming")
# Question 3
print("Question 3")
arg1 = sys.argv[1]
inputString = sys.argv[2]

def reverseStringCommandLine(arg1,inputString):
    if arg1 == '-r':
        return reverseString(inputString)
    elif arg1 == '-w':
        return revereStringOrder(inputString)
reverseStringCommandLine(arg1,inputString)

# Question 4
print("Question 4")
arg1 = sys.argv[1]
inputString = sys.argv[2]
textFile = open(os.path.dirname(os.path.realpath(__file__)) +'/'+ sys.argv[3])
fileInput = textFile.read()
def reverseStringCommandLineWithFileInput(arg1,inputString,fileInput):
    if fileInput == None and arg1 == '-w':
        return reverseString(inputString)
    elif fileInput == None and arg1 == '-r':
        return revereStringOrder(inputString)
    elif fileInput != None and arg1 == '-r':
        return reverseString(fileInput)
    elif fileInput != None and arg1 == '-w':
        return revereStringOrder(fileInput)    
reverseStringCommandLineWithFileInput(arg1,inputString,fileInput)
