def remove_and_strip(string,word):
    newstr= string.replace(word,"")
    return newstr.strip()

this = "   janhvi is programming"
n = remove_and_strip(this , "janhvi")
print(n)