#convert_g2oz.py
#A program to convert grams to ounces
#Author: Alex Heimann

def main():
    print "This program returns measurements in grams to ounces."
    #1 Gram = 0.03527396195 Ounces
    grams = input("Enter a measurement in grams: ")
    ounce_equivalent = grams * 0.03527396195
    print grams, "grams is equal to", ounce_equivalent, "ounces."
    
main()