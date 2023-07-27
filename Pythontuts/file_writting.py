#f = open("Janhvi.txt","w")# If such name file is not present it will create such file with respective name and if any file exisit it will erase all its text
#f = open("Janhvi.txt","a")
#a= f.write("Hi! It is wrtting program\n")#It return no. of characters
#print(a)
#f.close()

f = open("Janhvi.txt","r+") #'r+' means you want to use both read as well as write mode
print(f.read())
f.write("Thank you")
print(f.read())
f.close()