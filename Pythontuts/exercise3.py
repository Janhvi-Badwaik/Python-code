print("Guess the no. which is hidden")
print("You have 5 Chances to guess the no. \nSo Lets get started.")
count = 0
remaining = 5
num = 0
n=18
while(count<5 and remaining>0):
    print("Enter the no:",end=" ")
    num = int(input())
    if num>n and count<5 and remaining>0:
        print("Reduce a no.")
        count += 1
        remaining -= 1
       # print(count,remaining)
        print("Remaining chances are: ", remaining,"\n")
    elif num<n and count<5 and remaining>0:
        print("Increase a no.")
        count += 1
        remaining -= 1
       # print(count, remaining)
        print("Remaining chances are: ", remaining,"\n")
    elif num==n and count<5 and remaining>0:
        print("You got a correct no.")
        count += 1
        print("You took", count, " to guess")
        remaining -= 1
       # print(count, remaining)
        print("Remaining chances are: ", remaining,"\n")
        break


if count==5 and remaining==0 and num!=n:
    print("Game over ")
    print("You lost the match")
    print("Better luck next time!!")