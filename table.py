N = int(input("Enter the number to generate table : "))
i = 1
while i <= 10:
    print(N," * ",i," = ",(N*i))
    i+=1
    if i == 11:
        break
else :
    print("break")