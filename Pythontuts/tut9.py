#List are mutable means values can be change at any time,and can havae duplicate values.
grocery = ["harpic"," vim bar","Lollypop",561]
print(grocery)
print(grocery[0])
print(grocery[1])
numbers = [15,25,23,23,589,10223]
numbers.append(7456)
numbers.insert(0,89)
numbers.remove(25)
numbers.pop()
print(numbers[0:])
numbers.sort()
print(numbers)
print(numbers[0::2])
numbers.reverse()
print(numbers)
print(numbers[0::2])

#Tuple are immutable means values can not be change at any time,and can havae duplicate values.
tp = (2,89,15,657,2)
print(type(tp))
print(tp)
tp1 = (1)  # here it will work as int not as tuple
print(type(tp1))
print(tp1)
tp2 = (1,)   # to make it behave like tuple we only need to add "," after single element in tuple
print(type(tp2))
print(tp2)

# to swap two element in python we simply have to use below technique instead of using third variable
a = 22
b = 54
print(a,b)
a,b=b,a  # Python shortcut to swap two letters
print(a,b)