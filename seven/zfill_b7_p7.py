word=input("Enter a word: ")
width=int(input("Enter a width: "))
left="0"*(width-len(word))+word
print(left)