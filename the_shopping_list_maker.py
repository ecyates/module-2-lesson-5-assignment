# 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a function to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

# Create the grocery list as a global variable
grocery_list = []

# This function lets the user add as many items as they want to the grocery list
def addItems(*items):
    # Iterate through the input items
    for item in items:
        # Make sure we're not adding any duplicates
        while item not in grocery_list:
            # Add the item to the list
            grocery_list.append(item)

# This function lets the user remove as many items as they want from the grocery list
def removeItems(*items):
    # Iterate through the input items
    for item in items:
        # Only remove if the item is in the list
        while item in grocery_list:
            # Remove the item from the list
            grocery_list.remove(item)

# This function prints the grocery list as a bulleted list in alphabetical order
def printGroceryList():
    # Sort the list
    grocery_list.sort()
    print("Here are the items in your grocery list:")
    for item in grocery_list:
        print(f"\t- {item}")

# Creating the list - adding and removing items and then printing the list
addItems("apples", "bananas", "oranges")
# Checking what happens if you add multiple instances of the same item
addItems("olives", "bread", "eggs", "bread")
# Checking what happens if you remove an item not on the list
removeItems("cake")
removeItems("bread", "bananas")
printGroceryList()