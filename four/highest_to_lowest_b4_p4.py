# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
numbers = []
while True:
    inp = input("Enter number: ")
    if not inp.isdigit():
        break
    numbers.append(int(inp))
numbers.sort(reverse=True)
print(*numbers)