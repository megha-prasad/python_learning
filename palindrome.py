def isPalindrome(x):
    return x==x[::-1]
inp = input("Enter the string: ")
result = list(filter(isPalindrome,inp))
results=result[::-1]
print(result)
print(results)
if result == results:
    print("the palindrome is",''.join(results))
else :
    print("Not a palindrome")
