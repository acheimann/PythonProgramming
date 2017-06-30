#sphere_calc.py
#A program to calculate certain properties of sphere from a given measurement
#Such as volume and surface area

import math

def main():
    print "This program calculates the volume and surface area of a sphere, given its radius."
    print
    
    radius = input("Please enter the radius of your sphere: ")
    units = raw_input("Please enter the units of the radius you just entered: ")
    volume = 4/3*math.pi*radius**3
    surface_area = 4*math.pi*radius**2
    
    print "The volume of this sphere with radius", radius, "is", volume, "cubic", units
    print "The surface area of this sphere with radius", radius, "is", surface_area, "square", units
main()