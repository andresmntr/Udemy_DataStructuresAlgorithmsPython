"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) > 1:
        pivot = {"i": len(array)-1, "val":array[len(array)-1]}
        i=0
        while i < pivot["i"]:
            val = array[i]
            if val > pivot["val"]:
                array[pivot["i"]] = array[i]
                pivot["i"] -= 1
                array[i]=array[pivot["i"]]
                array[pivot["i"]] = pivot["val"]
            else:
                i+=1
        return quicksort(array[:pivot["i"]])+quicksort(array[pivot["i"]:])
    elif len(array)>0:
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)