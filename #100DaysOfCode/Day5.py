prs = str(input("Phrase: "))
prs = prs.split()

counter = 0
num = prs[0]

for i in prs:
    frequence = prs.count(i)
    if frequence > counter:
        counter = frequence
        num = i

print()
print(num)
