'''var1 = "Hello World"
var2 = 4
var3 = 36.7
var4 = "Janhvi"
var5 = "44"
var6 = "44"
print(type(var1))
print(type(var2))
print(type(var3))
print(var2+var3)#print(var1 + var2)#THis statement will give error because we can ad string and other data type
print(var1+var4)#This statemrnt won't give error
print(var1+var5)
print(int(var6)+int(var5))#Typecasting and getting answer
print(5 * "Janhvi\n")#Instead of using for loop to print text for 10 we can simply multiply it by 10(As we here multiply it with string )
print(10 * int(var6)+int(var5))#Here if we multiply it by 10 ,it will multyply the the value instead of printing it for 10 times because here we are multiplying with integer
print(10*str(int(var6)+int(var5)))
print("Enter your no")
InNum = input()#in Python input is receive in string even you enter any thpe of datatype as input
print("You Enter no ",int(InNum)+10)#for further calution with input type the input with respective datatype'''
print("Let's perform addition of two no. ")
print("Enter no. 1:")
num1 = input()
print("Enter no. 2:")
num2 = input()
print("Addition of ",num1 ," and ",num2," is ",(int(num1)+int(num2)))