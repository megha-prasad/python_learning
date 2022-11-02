def convert_int(x):
    return int(x)
mylist = ['1','2','3']
result = list(map(convert_int,mylist))
print(result)
