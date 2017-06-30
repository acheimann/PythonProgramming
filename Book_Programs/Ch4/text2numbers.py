#text2numbers.py
#A program to convert a textual message into a sequence of numbers
#utilizing the underlying ASCII coding

def main():
    print "This program converts a textual message into a sequence"
    print "of numbers representing the ASCII encoding of the message."
    print
    
    #get the message to encode
    
    message = raw_input("Please enter the message you wish to encode: ")
    
    print
    print "Here are the ASCII codes:"
    
    #loop through the message and print out the ASCII values
    for ch in message:
        printord(ch), #use comma to print all on on line
        
    print
    
main()
    