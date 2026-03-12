num1 = int(input("Enter first number: "))
num2 = int(input("Enter last number: "))
for i in range(num2 - num1- 1):
    num1 += 1
    print(num1, end=",")