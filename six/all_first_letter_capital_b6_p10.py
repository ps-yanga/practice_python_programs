cap=input("Enter a sentence: ")
word=cap.split()
letter=[]
for words in word:
    if words:
        letter.append(words[0].upper()+words[1:].lower())
print("".join(letter))
