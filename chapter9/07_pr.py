content = "true"
i=1
with open("log.txt") as f:
  
    while content:
        content = f.readline()
        #print(content)
        if 'python' in content.lower():
            print("Yes python is present")
            print(i)
        i+=1    
     

    
