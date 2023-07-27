with open("Janhvi.txt") as f: #instead of using 'open() and 'close()' method we can use this statement .here we don't need to close the file every time as it is controlled by this statement
   # a = f.read(4)
    #print(a)
    print(f.read())


f = open("Janhvi.txt","rt")
print(f.readlines())
print(f.readline())

f.close()