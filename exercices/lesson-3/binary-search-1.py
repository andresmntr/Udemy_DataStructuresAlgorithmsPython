"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value, pos):
    """Your code goes here."""
    if len(input_array) < 2:
        if input_array[0] == value:
            return pos
        else:
            return -1
    else: 
        middle = int(len(input_array)/2)
        if input_array[middle] == value:
            pos += middle
            return pos
        elif input_array[middle] > value:
            little_array = input_array[:middle]
        else:
            pos += middle
            little_array =  input_array[middle:]
        return binary_search(little_array, value, pos)
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1, 0)
print binary_search(test_list, test_val2, 0)