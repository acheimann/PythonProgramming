#ladder.py
#Compute the necessary length of a ladder to reach a certain height
#given the angle at which the ladder rests

import math

def main():
    print "This program will help you calculate the length of a ladder required to reach a certain height."
    print
    
    height = input("Please enter the height you need to reach: ")
    angle_degree = input("Please enter the angle in degrees: ")
    angle_radian = math.pi/180 * angle_degree
    length = height/math.sin(angle_radian)
    
    print "At an angle of", angle_degree, "degrees, you will need a latter that is approximately", round(length, 4), "feet long." #rounds the length to 4 decimal places for convenience
    
main()
    