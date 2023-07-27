'''var1 = 6
var2 = 56
var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")'''

''''list1 = [5,7,3]
print(5 in list1)
print(15 in list1)
print(5 not in list1)
print(15 not in list1)
if 5 in list1:
    print("Yes its in the list")
else:
    print("No it's not in the list")


#qize
print("To check whether your age is appropriate to drive vehical or not, \nEnter your age:")
age = int(input())
if age>18 and age<70:
    print("Eligible to drive")
elif age==18:
    print("We can't say anything , You have to visit our office for acknowledgement ")
else:
    print("Not Eligible to drive ")'''''

#faulty calculator

flage=1
while(flage):
    print("Enter no. 1")
    num1 = int(input())
    print("Enter no. 2")
    num2 = int(input())
    print("Enter the operator as per your choice")
    op = input()
    if num1 == 45 and num2 == 3 and op == '*':
        print("555")
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    elif num1 == 56 and num2 == 9 and op == '+':
        print("77")
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    elif num1 == 56 and num2 == 6 and op == '/':
        print("4")
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    elif num1 != 45 and num2 != 3 and op == '*':
        print(num1 * num2)
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    elif num1 != 56 and num2 != 9 and op == '+':
        print(num1 + num2)
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    elif num1 != 56 and num2 != 6 and op == '/':
        print(num1 / num2)
        print("To continue enter '1' and \nTo exit enter '0'")
        flage = int(input())
    else:
        print(num1 - num2)
        print("To continue enter '1' and \nTo exit enter '0'")
        flage=int(input())
