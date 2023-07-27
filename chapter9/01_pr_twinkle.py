f = open('poem.txt')
t = f.read()
if  'twinkle' in t:
    print(" 'twinkle' word is present ")
else:
    print(" 'twinkle' word is not present ")
f.close() 