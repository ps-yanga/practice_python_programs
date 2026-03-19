# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
from collections import Counter
numbers = []
while True:
    inp = input("Enter number: ")
    if not inp.isdigit():
        break
    numbers.append(int(inp))
most_common = Counter(numbers).most_common(1)[0][0]
print("most duplicate:", most_common)