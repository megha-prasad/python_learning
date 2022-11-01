def my_func(studRoll):  #ftn header; defining ftn
    """printing the roll number of the student"""
    print("student roll number is", studRoll)
    return  #used to exit from the function
my_func(1648532)    #passing arguments

def new_ftn():
    my_list=[1,2,3,4]
    s = sum(my_list)
    return s
result = new_ftn()
print("result is ",result)

def new_ftn2(myList):
    s = sum(myList)
    return s
result = new_ftn2([1,2,3,4])
print("result is ",result)

def squareOdd():
    """prgm to print squares of odd numbers"""
    square = [x**2 for x in range(1,11) if x%2==1]
    return square
squares = squareOdd()
print("the squares are ", squares)

#  WRONG CODE !!!!
def maxnum(newlist):
    """to print the max from a list"""
    maxi = max(newlist)
    return maxi
maxim = maxnum((input("enter the list : ")))
print(maxim)

#CORRECT CODE
n=int(input("Enter number of element in list"))
mylist=[]
print("Enter elements of the list")
for _ in range(n):
    a=int(input())
    mylist.append(a)
maximum=max(mylist)
print("Maximum of the list is :",maximum)

#variable number of argument
def ftn(*args):
    pass
ftn(1,"hi",3)

def add(*a):
    print(sum(a))
    return
add(1,2)
add(1,2,3)

def fun(a,b,c):
    print("a=",a,"b=",b,"c=",c)
    return
t = (1,2,3) #tuple
fun(*t)

def fun1(e,f,g):
    print("e=",e,"f=",f,"g=",g)
    return
d = {"e":1,"f":2,"g":3} #dict
fun1(**d)