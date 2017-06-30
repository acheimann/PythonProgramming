# File: chaos.py
# A simple program illustrating chaotic behavior.

#Currently incomplete: advanced exercise 1.6 
#Exericse 1.6 is to return values for two numbers displayed in side-by-side columns

def main(): 
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    y = input ("Enter a second number between 0 and 1:")
    n = input("How many numbers should I print?")
    for i in range(n):
        x = 2.0 * x * (1 - x)
        print x
        y = 2.0 * y * (1-y)
        print y
        
main()