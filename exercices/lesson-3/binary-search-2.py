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

def binary_search(input_array, value):
    i = int(len(input_array)/2)
    aux = 1
    while aux < int(round(len(input_array)**(.5))):
        """Your code goes here."""
        aux +=1
        if (input_array[i]==value):
            return i
        elif (input_array[i]>value):
            i = int(i/2)
        elif (input_array[i]<value):
            i = i + int(i/2)
    return -1
    
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)