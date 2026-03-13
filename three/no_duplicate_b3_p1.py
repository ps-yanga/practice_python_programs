# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
number=[]
for i in range (10):
    num = int(input("Enter number: "))
    number.append(num)
dup=(set(number))
print(dup)