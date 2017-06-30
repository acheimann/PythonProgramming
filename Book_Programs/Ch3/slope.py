#slope.py
#calculates the slope of a line passing between two points given their x and y coordinates

def main():
    print "This program calculates the slope of a line between two points."
    print
    
    x1,y1 = input("Please enter the x and y coordinates of your first point: ")
    x2, y2 = input("Please enter the x and y coordinates of your second point: ")
    
    slope = float(y2-y1)/float(x2-x1)
    print "The slope of the line between these two points is", slope

main()