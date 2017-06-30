#pi_approx.py
#A program to approximate the value of pi

import math

def main():
    print "This program approximates the value of pi."
    print
    
    pi_estimate = 0
    n = input("Please enter how many terms you wish to sum: ")
    for i in range(n):
        pi_estimate = pi_estimate + 4.0 * (-1)**i/(2*i + 1)
        error_difference = math.pi - pi_estimate
        percent_accuracy = error_difference/math.pi

        print "Using", n, "terms, the value of pi is calculated to be", pi_estimate
        print "The difference between this value and pi is", error_difference
        if percent_accuracy >= 0:
            print "That is an overestimation of", percent_accuracy * 100,"percent."
        else:
            print "That is an underestimation of", abs(percent_accuracy * 100), "percent."

main()
      