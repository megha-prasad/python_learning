def isGreater(x):
    return x>5
myList=[12,5,4,26,6,7,3,1,25,39,58]
result = list(filter(isGreater,myList))
print(result)