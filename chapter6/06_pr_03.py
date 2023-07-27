from multiprocessing.spawn import spawn_main


text = input("Enter the text")
if ("Make  alot of money" in text):
    spam = True
elif("by now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
else:
    spam = False

if spam:
    print("it is an spam")
else:
    print("it is not an spam")