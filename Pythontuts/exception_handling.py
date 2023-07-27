num1 = input("Enter no.1")
num2 = input("Enter no.2")
try:
    print("Sum is",(int(num2)+int(num1)))

except Exception as e:
    print(e)


print("Both input should be integer")