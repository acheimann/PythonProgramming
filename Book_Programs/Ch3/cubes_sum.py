#cubes_sum.py
#sum the cubes o natural numbers

def main():
    n = input("Please enter the desired number of natural numbers to be included: ")
    for i in range(n+1):
        i = (i**2*(i+1)**2)/4
        
    print "The sum of the cubes of the first", n, "natural numbers is", i
    
main()