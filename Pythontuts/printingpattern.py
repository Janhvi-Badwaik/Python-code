n = int(input(("Enter a no.:")))
n2 = int(input("Enter '0' or '1':"))
b=bool(n2)
print(b)
if b == True:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

else:
    for i in range(n,0):
        for j in range(0,i+1):
            print("*",end="")
        print()