#triangle_area.py
#A program to calculate the area of a triangle given the lengths of its sides

import math

def main():
    print "This program calculates the area of a triangle given the lengths of its sides."
    print
    
    a, b, c = input("Please enter the lengths of the sides of the triangle: ")
    units = raw_input("Please enter the unit of measurement for the sides provided above: ")
    s = float(a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print "The area of the triangle is", area, "square", units
    
main()