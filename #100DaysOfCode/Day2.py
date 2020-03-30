num = int(input("Número: "))
divOfNum = []
sum = 0

for i in range(0,num):
    if num % (num - i) == 0 and i != 0:
        sum += (num - i)
        divOfNum.append((num - i))

if sum == num:
    print(num , "is a Perfect Number")

else:
    print(num , "isn't a Perfect Number")
