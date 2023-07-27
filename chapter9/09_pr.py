with open("this.txt",'r') as f:
    content=f.read()
with open("copythis.txt",'r') as f1:
    content1=f1.read()

if content==content1:
    print("files are same")
else:
    print("files are not same")