#quadratic.py
#Illustrates use of the math library
#Note: The program crashes if the equation has no real roots

import math #makes math library available

def main():
    print "This program finds real solutions to a quadratic"
    print
    
    a, b, c = input("Please enter the coefficients (a, b, c): ")
    
    discriminant = b*b - 4*a*c
    discRoot = math.sqrt(discriminant)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)
    
    print
    #conditional statement intended to return custom error message for values with no real solution
    #currently python throws math domain error when calling the sqrt function
    #so the program crashes before the else statement ever comes into effect
    if discriminant > 0.0:
        print "The solutions are:", root1, "and", root2
    else:
        print "Error: the values you entered have no real solution"
    
main()