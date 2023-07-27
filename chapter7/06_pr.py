num=int(input("Enter number to find factorial of it :- "))
f=1
for i in range(1,num+1):
    f=f*i
print(f"The factorial of {num} is {f}")