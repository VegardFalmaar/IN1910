def less_than(original, n):
    newlist = [element for element in original if element < n]
    return newlist


print (less_than([1, 2, 3, 4, 5], 3))
print (less_than([1, 2, 3, 4, 5], 4))
print (less_than([1, 2, 3, 4, 5], 5))
print (less_than([1, 2, 3, 4, 5], 6))