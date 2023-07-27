d1 = {"Combination":"union","Permutation":"Arrangement","Introvert":"Shy","Ambivert":"Person who has a balance of extrovert and introvert"}
print("Enter the following words to get its meaning \n 1.Combination\n 2.Permutation\n 3.Introvert\n 4.Ambivert")
value = input("Enter the following words to get its meaning \n 1.Combination\n 2.Permutation\n 3.Introvert\n 4.Ambivert")
if value in d1:
    print(d1[value])
else:
    print("Enter valid word.")
