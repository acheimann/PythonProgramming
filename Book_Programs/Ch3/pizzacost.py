#pizzacost.py
#calculates the cost per square inch of pizza

import math

def main():
    print "This program calculates the cost per square inch of pizza."
    print
    
    diameter = input("Please enter the diameter of the pizza in inches: ")
    price = input("Please enter the price of the pizza: ")
    radius = diameter/2
    area = math.pi*radius**2
    cost_per_square_inch = price/area
    price_per_square_inch = round(cost_per_square_inch, 2) #rounds the cost figure to the nearest cent
    print "You will pay", price_per_square_inch, "per square inch for this pizza."
    print "If you want to be more exact, this pizza costs", cost_per_square_inch, "per square inch."
    
main()