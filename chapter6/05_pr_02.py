a1 = int(input("Ente your Marks for Subject 1 "))
a2 = int(input("Ente your Marks for Subject 2 "))
a3 = int(input("Ente your Marks for Subject 3 "))
if (a1<33 or a2<33 or a3<33):
    print("You are failed because you have marks less than 33")
elif ((a1+a2+a3)/3)<40:
    print("you are failed per is less than 40%") 
else:
    print("You are passed")