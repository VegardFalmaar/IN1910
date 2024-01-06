def bubble_sort(input):
    """Returns a new list with the data from input list/tuple in sorted order."""
    newlist = list(input[:])
    for i in range(1, len(input)):
        for j in range(len(input)-i):
            if newlist[j+1] < newlist[j]:
                newlist[j+1], newlist[j] = newlist[j], newlist[j+1]
    return newlist

print (bubble_sort([3]))