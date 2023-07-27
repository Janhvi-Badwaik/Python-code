f=open("Janhvi.txt","rt")
#c = f.read()
#print(c)
#print(f.readline())#this also one way to print one line at a time instead of read method
#for line in f:#we can read the file without using a read method
    #print(line,end="")
#print(f.readlines())#due to this method we can print all line at a time
#print(f.tell())#'tell()' method tells about that where our file pointer.
print(f.readline())
#print(f.tell())
f.seek(3)#take the file pointer to respective index in file
print(f.readline())
#print(f.tell())

f.close()