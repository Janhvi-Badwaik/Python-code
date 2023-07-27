# Dictonary is case-sensitive,Keys are immutable,It can be Number or character

d1 = {}
print(type(d1))
d2 = {"Janhvi":"Flower","Jitesh":"Animal","Savita":"Travel","Jiwan":"Eating"}
print(d2)
print(d2["Janhvi"])
d3 = {"Janhvi":"Flower","Jitesh":"Animal","Savita":"Travel","Jiwan":"Eating","Ram":{"B":"Sandwich","L":"Dal","D":"Chiken"}}
print(d3["Ram"])
print(d3["Ram"]["B"])
d3.update({"Leena":"pane-pruri"}) # another way to update your dictonary
print(d3)
d3["Ankit"]={"Junk Food"} # adding another key and value to dictonary
print(d3)
del d3["Ankit"] # "del" keyword is used to delete any value from dictonary
print(d3)
d4=d3 # here actually 
del d4["Ram"]
print(d3)
print(d3.items())

