my_list = []
my_list=[i for i in range(10)]
print(my_list)

#OR
# for i in range(10):
#   my_list.append(i)
# print(my_list)

#generate square odd nums
# [x**2 for x in range(1,11) if x%2==1]
#
#if else with list comprehension
# ["even" if x%2==0 else "odd" for x in range(10)]