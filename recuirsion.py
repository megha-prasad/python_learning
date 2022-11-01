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

#to calculate the sum of digits:
#n = input number
#x=n%10 --> to get the last digit of the input number
#n=n//10

def ftn1(k):
    if k == 0:
        return 0
    else:
        return k%10+ftn1(k//10)
result1 = ftn1(int(input("enter the number: ")))
print(result1)
