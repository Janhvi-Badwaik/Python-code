with open('sample.txt','r') as f:
    content = f.read()

content=content.replace("#######","twinkle")
with open('sample.txt','w') as f:
     f.write(content)