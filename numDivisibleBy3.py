#Write a pgm to print values from 1-30, but not include numbers which are divisible by 3
for i in range(1,31):
    if i%3==0:
        continue
    print(i, end=" ")
print("\nend of pgm")