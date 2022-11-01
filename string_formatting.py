s ="Python"
i = 1991
print(s," was developed in ",i) #normal method
print("%s was developed in %d"%(s,i)) #fromatting
print("%s"%(s))
print("%15s"%(s))
print("%-15s"%(s))
print("%0.5s"%(s))#truncate to 5 characters
#%f for float
# padding
print("%4d"%(42))
print("%04d"%(42)) #padding with zero
print("%4d"%(42))
print("%06.2f"%(42854.745146895368))


#new method
print("{:>15}".format(s))
print("{:<15}".format(s))
print("{:^15}".format(s))#centre
print("{:-^15}".format(s))
print("{:.5}".format(s))

print("hi {}, my name is {} and my age is {}".format("there", "megha", 22))
print("hi {1}, my name is {0} and my age is {2}".format("june", "megha", 22))