#numbers2text.py
#A program to convert a sequence of ASCII numbers
#into a string of text

import string #include string library for the split function

def main():
    print "This program converts a sequence of ASCII numbers into"
    print "The string of text that it represents."
    print
    
    #Get the message to encode
    inString = raw_input("Please enter the ASCII-encoded message: ")
    
    #loop through each substring and build ASCII message
    msgList = [] #creates list to which converted ASCII values will be temporarily appended
    message = ""
    for numStr in string.split(inString):
        asciiNum = eval(numStr) #convert digits to a number
        msgList.append(chr(asciiNum)) #appends characters to temporary msgList
        message = string.join(msgList,"") #joins elements of msgList
        
    print "The decoded message is:", message
    
main()

#STring: 83 116 114 105 110 103 115 32 97 114 101 32 70 117 110 33