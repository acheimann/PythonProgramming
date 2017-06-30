#gregorian_epact.py
#Calculates the Gregorian epact (number of days between January 1 and previous new moon)
#Used to calculate the date of Easter

def main():
    print "This program returns the value of the Gregorian epact."
    print
    year = input("Please enter the current year in four-digit format: ")
    C = year/100
    epact = (8 + (C/4) - C +((8*C+13)/25) + 11*(year%19))%30
    
    print "This year's epact value is", epact
    
main()