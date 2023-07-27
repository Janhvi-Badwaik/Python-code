Name = input("Enter your Name \n")
date = input("Enter your date \n")
letter = ''' Dear <|Name|>,
You are selected!

Date:<|date|>
'''
letter = letter.replace("<|Name|>" , Name)
letter = letter.replace("<|date|>" , date)
print(letter)