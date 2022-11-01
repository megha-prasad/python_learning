#break statement
#for i in range(1,11):
#   if i == 5:
#      break
#    print(i)
#print("end of pgm")

#Break statement in nested loop
#for i in range(1,5):
#    for j in range(1,5):
#        if i == 3:
#            break
#        print("i = ", i," end of inner loop")
#    print("end of outer loop")
#print("end of pgm")

#searching for an element
newlist = [23,85,12,6,98]
n = int(input("Enter the input value : "))
for i in newlist:
    if i == n :
        print("Value found")
        break
    print(i)
else:
    print("value is not found")
print("end of program")

#CONTINUE
for i in range(10):
    if i == 5:
        continue
    print(i)
print("end of the program")
