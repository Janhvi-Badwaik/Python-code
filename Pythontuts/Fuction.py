a = 9
b = 10
c= sum( (a , b) )  #build in function
print(c)

def func1(a,b):
    print("Addition of two no. are ",(a+b))


def func2(a,b) :
    """ This is average function """ #DocString it work as a string as well as like instructiion
    avg=(a+b)/2
    print(avg)
    return avg



print(func2.__doc__)
v = func2(7,8)
print(v)