upper=input("Enter a word: ")
letter=""
for char in upper:
    if 'a' <= char <= 'z':
        letter+=chr(ord(char)-32)
    else:
        letter+=char
print(letter)