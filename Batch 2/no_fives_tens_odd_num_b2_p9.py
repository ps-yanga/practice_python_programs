odd = 0
while odd < 100:
    if odd % 2 != 0 and odd % 5 != 0:
        print(odd, end=",")
    odd += 1