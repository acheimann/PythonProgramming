#sum_series.py
#A program to sum a series of natural numbers entered by the user

def main():
    print "This program sums a series of natural numbers entered by the user."
    print
    
    total = 0   
    n = input("Please enter how many numbers you wish to sum: ")
    for i in range(n):
        number = input("Please enter the next number in your sequence: ")
        total = total + number

    print "Your total adds up to", total

main()
      
      