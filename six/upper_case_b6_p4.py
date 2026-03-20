upper=input("Enter a sentence: ")
casing=True
for char in upper:
    if char.isalpha() and not ('A' <= char <= 'Z'):
        casing=False
        break
print(casing)