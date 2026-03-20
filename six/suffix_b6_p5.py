word=input("Enter a word: ")
suffix=input("Enter a suffix: ")
ends_with=len(s)>=len(suffix) and s[-len(suffix):]==suffix
print(ends_with)