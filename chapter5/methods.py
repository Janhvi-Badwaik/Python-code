myDict = {
    "Fast": "In a Quick Manner",
    "Janhvi": "A girl",
    "Marks": [1,2,3,5],
    "Anotherdict":{ 'harry':'Palyewr'},
    1: 2
    }
print(myDict.keys())#printes the keys of dictonory
print(type(myDict.keys()))
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
updateDict = {
    'Lovish': 'spread love'
}
print(myDict.update(updateDict)) #--->Don't work gives none
myDict.update(updateDict)
print(myDict)
print(myDict.get("Janhvi"))#---> Output are same but if u enter different non present key
print(myDict.get("Janhvi1"))# returns 'none'
print(myDict["Janhvi"])     #---get fuction will return 'None' but without get fuction it will retuen error
print(myDict["Janhvi1"])  #returns error