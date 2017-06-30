#storm_distance.py
#Calculates the distance of a lightning strike based on time between flash and thunder

def main():
    print "This program calculates the distance of a lightning strike"
    print "based on the time elapsed between the flash and the sound of thunder."
    
    time_since_flash = input("Please enter the number of seconds since the lightning flash: ")
    lightning_distance = float(time_since_flash) * 1100 / 5280 #calculates distance in feet by multiplying time elapsed by speed      of sound - 1100 feet per second
    #converts distance to miles by dividing by number of feet in a mile - 5280
    
    print "That lightning strike was", lightning_distance, "miles away."  

main()  

    
    
    