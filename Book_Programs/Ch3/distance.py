#distance.py
#calculates the distance betweeen two points given their coordinates

import math

def main():
    print "This program calculates the distance between two points."
    print
    
    x1, y1 = input("Please enter the x and y coordinates of your first point: ")
    x2, y2 = input("Please enter the x and y coordinates of your second point: ")
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print "The distance between these two points is", distance
    
main()