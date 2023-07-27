myDict = {
    "Fast": "In a Quick Manner",
    "Janhvi": "A girl",
    "Marks": [1,2,3,5],
    "Anotherdict":{ 'harry':'Palyewr'}
    }
print(myDict['Fast'])
print(myDict['Janhvi'])
print(myDict['Anotherdict'])
print(myDict['Anotherdict']['harry']) #--->nested dictionary
myDict['Marks'] = [1,2,3,4,5,6,7]
print(myDict['Marks'])