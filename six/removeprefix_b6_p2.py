remove=input("Enter sentence:")
prefix=input("Enter prefix to remove:")
if remove.startswith(prefix):
    remove=remove[len(prefix):]
print(remove)