from functools import reduce
import operator

myList = [1,2,3,4,5,6,7,8,9]
result1 = reduce(lambda x,y:x+y, myList)
result2 = reduce(operator.add, myList)
result3 = reduce(operator.mul, myList)
print(result1)
print(result2)
print(result3)