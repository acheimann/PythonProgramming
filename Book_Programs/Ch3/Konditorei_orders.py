#Konditorei_orders.py
#Calculates the cost of an order of coffee for the Konditorei coffee shop.

def main():
    
    print "This program determines the total cost of your order"
    print "based on the cost of the coffee and the cost of shipping."
    print
    
    order_size = input("Please enter the number of pounds of coffee you wish to order today: ")
    coffee_cost = order_size*10.50
    shipping_cost = 1.50 + order_size*0.86
    total_cost = coffee_cost + shipping_cost
    
    print "Thank you for ordering from Konditorei Coffee Shop!"
    print "Your total is:"
    print
    print "Coffee:", round(coffee_cost, 2)
    print "Shipping:", round(shipping_cost, 2)
    print "Total:", round(total_cost, 2)
    print
    print "Enjoy your coffee!"

main()
    