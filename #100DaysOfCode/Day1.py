num = int(input("Number: "))
num = str(num)
sum = 0
mul = 1
for i in range(0,len(num)):
    newNum = int(num[i])
    sum = sum + newNum

for i in range(0,len(num)):
    newNum = int(num[i])
    mul = mul * newNum

if mul == sum:
    print()
    print(num + " is a Spy Number")
else:
    print()
    print(num + " isn't a Spy Number")
