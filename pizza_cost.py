#!/usr/bin/env python3
# Created By: Beni
# Date: March 4, 2025
# Calculates the cost of a pizza

import math
import constants

def main():
    pizza_diameter = float(input("What is the diameter of the pizza?: "))
    subtotal = pizza_diameter * 1.5 + 4.25
    tax = subtotal * constants.TAX
    total = subtotal + tax

    print("A pizza with a diameter of {},". format (pizza_diameter), 
          "has a subtotal of {}" . format (subtotal), 
          "and creates a tax of {:.2f}". format (tax), 
          "for a total cost of {:.2f}". format (total))
    
if __name__ == "__main__":
    main()
