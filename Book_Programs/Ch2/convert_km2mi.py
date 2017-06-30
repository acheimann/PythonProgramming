#convert_km2mi.py
#A program to convert measurements in kilometers to miles
#author: Alex Heimann

def main():
    print "This program converts measurements in kilometers to miles."
    km_distance = input("Enter the distance in kilometers that you wish to convert: ")
    mile_equivalent = km_distance * 0.62
    print km_distance, "kilometers is equal to ", mile_equivalent, "miles."
    
main()