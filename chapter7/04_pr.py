num = int(input("Enter the number:-"))
prime=True
for i in range(2,num):
    if (num%i==0):
        print(i)
        prime=False
        break
if prime:
    print(str(num)+" is prime")
else:
    print(str(num)+" is not a prime")