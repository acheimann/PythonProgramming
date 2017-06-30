#futval.py
#A program to compute the value of an investment
#carried 10 years into the future

def main():
    print "This program calculates the future value"
    print "of a ten-year investment."
    
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate: ")
    period = input("Enter the number of compounding periods for your interest rate: ")
    deposit = input("Enter the amount you wish to add to your investment annually: ")
    duration = input("Enter the number of years for which you wish to invest your money: ")
    
    for i in range(duration * period):
        principal = (principal + deposit/period) * (1+(apr/period)
    print "The value in ", duration, " years is $", principal
        
main()