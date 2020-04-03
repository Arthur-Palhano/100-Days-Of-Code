
num = int(input("Number: "))
original = num
bin = ""
while num > 1:
    if num % 2 == 0:
        num = num/2
        bin += "0"
    elif num % 2 == 1:
        num = (num - 1)/2
        bin += "1"

if original == 0:
    bin = "0"
else:
    bin += "1"
    bin = bin[::-1]
i = bin.count("1")
print(f"O número {original} em binário equivale à {bin} e possui {i} 1's")
