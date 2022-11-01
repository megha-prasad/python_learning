# to find factorial using iterative method

#n = int(input("enter the number : "))
#fact = 1
#for i in range(1,n+1):
#    fact = fact*i
#    i = i+1
#print(fact)

#using recursive function
def ftn(n):
    if n==0: #base condition
        return 1
    else:
        return n*ftn(n-1)
result = ftn(int(input("enter the number : ")))
print(result)
