def mySquare(x):
    return x*x
def myCube(x):
    return x*x*x
def calculate(ftn,arg):
    print(ftn(arg))
calculate(mySquare,2)
calculate(myCube,2)

def calcu():
    def squar(arg1):
        print(arg1*arg1)
    return squar
d=calcu()
d(2)

#using lambda
def calcul():
    lambda arg2:arg2*arg2
d=calcu()
print(d(2))
