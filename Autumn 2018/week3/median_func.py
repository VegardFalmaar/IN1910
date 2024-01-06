def median(data):
    """Returns the median of a dataset."""
    newlist = list(data[:])
    newlist.sort()
    if len(newlist)%2 == 0:
        i = len(newlist)//2
        res = (newlist[i-1] + newlist[i])/2
    else:
        res = newlist[len(newlist)//2]
    return res

# print(median([11, 3, 1, 5, 3]))
# print (4//2)