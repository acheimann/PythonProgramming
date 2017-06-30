#dateconvert.py
#converts a date in form "mm//dd/yyyy" to "month day, year"

import string

def main():
    #get the date
    dateStr = raw_input("Enter a date (mm/dd/yyyy): ")
    
    #split string into components
    monthStr, dayStr, yearStr = string.split(dateStr, "/")
    
    #convert monthStr to month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    montStr = months[int(monthStr) - 1]
    
    #output result in month day, year format
    print "The converted date is:", monthStr, DayStr+",", yearStr
    
main()