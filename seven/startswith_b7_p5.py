check=input("Enter a word: ")
prefix=input("Enter a prefix: ")
starts_with=len(check)>=len(prefix) and check[:len(prefix)]==prefix
print(starts_with)