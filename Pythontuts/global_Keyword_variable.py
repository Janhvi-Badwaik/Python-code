'''l=10 #goble scope variable
def fun1(n):
    #l=5 #local variable
    m=8 # local variable
    global l #global key word gives the permission to cange the value of any global variable in method
    l= l+45
    print(l,m)
    print(n, "I have printed")

fun1("This is me")
print(l)'''
x=89
def fun2():
    x=56
    def fun3():
        global x
        x=88
    print("Befor calling fun3()",x)
    fun3()
    print("After calling fun3()",x)
print(x)
fun2()
print(x) # it will search for global variable first then for local variable
