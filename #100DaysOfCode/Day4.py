prs = str(input("Phrase: "))
prs = prs.split()
Phrase = ""
shd = []

for i in range(0,len(prs)):
    if prs[i] not in shd:
        shd.append(prs[i])
        Phrase += prs[i] + " "

del(shd[len(shd)-1])
print(Phrase)
