#!/usr/bin/env python3


# Note that a discount is calculated as a percentage off of the total cash register price (e.g. a discount of 20 means the customer receives 20% off of their total price).

# Hint #1: Keep in mind that to access an attribute or call an instance method inside another instance method, we use the self keyword to refer to the instance on which we are operating. For example:

# class Person:

#   def __init__(self, age=0):
#     self.age = age

#   def birthday(self):
#     self.age += 1
# Follow along with the tests in lib/testing/cash_register_test.py. Reading along with what the tests are looking for can be really helpful!

# Take it one step at a time!

# Hint #2: The apply_discount() method requires some knowledge about working with integers versus floats in Python. When you get to that method, take a look at what return value the tests are expecting and keep in mind that Python provides methods for changing an Integer to a Float and vice versa.

# Hint #3: The void_last_transaction() method will remove the last transaction from the total. You'll need to make an additional attribute and keep track of that last transaction amount somehow. In what method of the class are you working with an individual item?

# Hint #4: Python handles mutable default values for arguments differently than it handles immutable default values. This means that you should usually not set default values for lists, dictionaries, and instances of classes. You can learn more on this quirk in Python's documentation on More Control Flow Tools Links to an external site..

# This tool needs to be loaded in a new browser window

class CashRegister:
    def __init__(self, discount=0.0):
        """
        Initialize the cash register.
        :param discount: An optional discount percentage.
        """
        self.items = []  
        self.total = 0.0  
        self.last_transaction_amount = 0.0 
        self.last_transaction_items = []  
        self.discount = discount  

    def add_item(self, item, price, quantity=1):
        """Adds an item to the register."""
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction_amount = transaction_total
        self.last_transaction_items = [(item, price, quantity)]
        self.items.extend([item] * quantity)
        return self.total

    def apply_discount(self):
      """Applies the discount to the total."""
      if self.discount > 0:
          discount_amount = self.total * (self.discount / 100)
          self.total -= discount_amount
          print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
          print("There is no discount to apply.")


    def void_last_transaction(self):
        """Voids the last transaction."""
        if self.last_transaction_items:
            self.total -= self.last_transaction_amount
            for item, price, quantity in self.last_transaction_items:
                for _ in range(quantity):
                    self.items.remove(item)
            self.last_transaction_amount = 0.0
            self.last_transaction_items = []
        else:
            return "No transaction to void."

    def get_total(self):
        """Returns the current total."""
        return self.total






register = CashRegister(20)

# Adding items
register.add_item("apple", 1.00, 3)
register.add_item("banana", 0.50, 2)
print(f"Total after adding items: ${register.get_total():.2f}")

# Applying discount
print(register.apply_discount())  


register.void_last_transaction()
print(f"Total after voiding last transaction: ${register.get_total():.2f}")
