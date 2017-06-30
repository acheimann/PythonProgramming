 #convertf2c
 #A program to convert fahrenheit temperatures to Celsius
 #author: Alex Heimann
 
def main():
     print "A program to convert fahrenheit temperatures to Celsius"
     print "for the rest of the world besides America"
     fahrenheit = input("Enter the temperature in degrees Fahrenheit: ")
     celsius = (5.0/9.0) * (fahrenheit - 32.0)
     print "The temperature is ", celsius, "degrees Celsius."
     
main()