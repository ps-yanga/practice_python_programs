name=input("Enter your name: ")
snake_case="_".join(word.lower() for word in name.split())
print(snake_case)