#average_series.py
#A program to calculate the average of a series of natural numbers entered by the user

def main():
    print "This program calculates the average of a series of natural numbers entered by the user."
    print
    
    total = 0   
    n = input("Please enter how many numbers you wish to include: ")
    for i in range(n):
        number = input("Please enter the next number in your sequence: ")
        total = total + number
        average = total/n

    print "The average of your sequence is", average

main()
      