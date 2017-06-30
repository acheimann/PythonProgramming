#sqrt_estimator.py
#A program to estimate the square root of a number
#using Newton's method

import math

def main():
    print "This program uses Newton's method to approximate the square root of a real number."
    print
    
    total = 0   
    n = input("Please enter a positive integer: ")
    guess = float(input("Please enter your best initial guess for the square root: "))
    attempts = input("Please enter the number of times you wish the program to continue guessing: ")
    
    sqrt_estimate = 0
    for i in range(n):
        sqrt_estimate = (guess + (attempts/guess))/2
        difference = math.sqrt(n) - sqrt_estimate
        percent_accuracy = difference/math.sqrt(n)
        
    print "Using Newton's formula, the square root of", n, "is calculated to be", sqrt_estimate
    print "The difference between this value and the actual square root is", difference
    if percent_accuracy >= 0:
        print "That is an overestimation of", percent_accuracy * 100,"percent."
    else:
        print "That is an underestimation of", abs(percent_accuracy * 100), "percent."

main()
      