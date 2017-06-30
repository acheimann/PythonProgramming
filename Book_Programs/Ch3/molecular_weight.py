#molecular_weight.py
#This program determines the weight of a hydrocarbon
#based on the number of hydrogen, carbon, and oxygen atoms it is composed of.

def main():
    print "This program determines the molecular weight of a hydrocarbon"
    print "based on its composition."
    print
    
    h = input("Please enter the number of hydrogen atoms in your molecule: ")
    c = input("Please enter the number of carbon atoms in your molecule: ")
    o = input("Please enter the number of oxygen atoms in your molecule: ")
    molecule_weight = h*1.0079 + c*12.011 + o*15.9994
    
    print "This molecule weighs", molecule_weight, "grams/mole."
    
main()