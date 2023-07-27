mystr = "Janhvi is good girl"
print(len(mystr))
print(mystr[0:19])
print(mystr[0:87])#Here it will not give error eventhough we are not having 887th index in mystr (here we intially with index which is present in mystr)
#print(mystr[78])#It will give error as there is no 78th index in mystr
print(mystr[0:19:2])
print(mystr[0::2])
print(mystr[:19:2])
print(mystr[::-1])#it reverse the string
