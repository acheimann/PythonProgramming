#natural_number_sum.py
#A program to sum as many natural numbers as the user requests

def main():
    n = input("Please enter how many natural numbers you wish to add up: ")
    for i in range(n+1):
        i = i*(i+1)/2
    
    print "the sum of the first", n, "natural numbers is", i
    
main()
        