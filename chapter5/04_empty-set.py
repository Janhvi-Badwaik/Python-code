a = {} #--->It is represents as empty dictonery not empty set
print(type(a))

#An empty set can be created using the below syntax:
b = set()
print(type(b))
b.add(1)
b.add(2)
b.add(3)
#b.add([4,5,6]) # dictonary & list dont work
b.add((4,5,6)) # tuple dont work
print(b)
print(len(b)) # prints the length of set
b.remove(3)
print(b)