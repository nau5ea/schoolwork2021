# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:25:58 2020

@author: Louis Moench IV
"""

def add_fruit(inventory, fruit, quantity):
    """Add the given quantity of fruit to the inventory.
    """
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

# Make these tests work
def add_fruit_test():
    print("Testing add_fruit")
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    assert "strawberries" in new_inventory
    assert new_inventory["strawberries"] == 10
    add_fruit(new_inventory, "strawberries", 25)
    assert new_inventory["strawberries"] == 35
    print("All tests pass!")

def count_letters(word):
    frequency = { }
    smallword = word.lower()
    for letter in smallword:
        if letter in frequency:
            frequency[letter] = frequency[letter] + 1
        else:
            frequency[letter] = 1
    return frequency

def print_frequencies(frequency):
    print("{0:>3.4s},{1:>4.4i}".format(frequency.values, frequency.keys))
