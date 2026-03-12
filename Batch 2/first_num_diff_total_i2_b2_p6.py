num1 = []
for i in range(10):
    num = int(input(f"Enter a number {i+1} : ",))
    num1.append(num)
print(num1[0] - sum(num1[1:]))
