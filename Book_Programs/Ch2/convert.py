#convert.py
#A program to convert Celsius temps to Fahrenheit
#by: author

def main():
    print "This program takes the temperature in degrees Celsius and returns it in degrees Fahrenheit"
    print "For all you Americans who insist on measuring temperatures in Fahrenheit"
    for i in range(5):
        celsius = input("What is the Celsius temperature? ")
        fahrenheit = (9.0/5.0) * celsius + 32
        print "The temperature is", fahrenheit, "degrees Fahrenheit."
    
main()