# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers = []
while True:
    inp = input("Enter number: ")
    if not inp.isdigit():
        break
    numbers.append(int(inp))
numbers.sort()
print(*numbers, end=", ")