#fibonacci.py
#A program to calculate the value of the first n terms of the Fibonacci sequence
#Where n is a value provided by the user

def main():
    print "This program calculates the value of the first n terms of the Fibonnaci sequence"
    print "where n is a value provided by the user."
    print
    
    n = input("Please enter how many terms of the Fibonacci sequence you wish to evaluate: ")
    fib1 = 0 #
    fib2 = 1
    
    for i in range(n):
        fib_temp = fib1
        fib1 = fib2 
        fib2 = fib_temp + fib1 
        
        
    print "The value of the first", n+2, "terms of the Fibonacci sequence is", fib2
    #n-2 is used because the first two values of the fibonacci sequence
    #are automatically assigned to fib1 and fib2

main()