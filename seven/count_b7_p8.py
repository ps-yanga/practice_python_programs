word=input("Enter a word: ")
substr=input("Enter a substring: ")
count=0
start=0
while True:
    pos=word.find(substr,start)
    if pos==-1:
        break
    count+=1
    start=pos+1
print(count)