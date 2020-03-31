prs = str(input("Phrase: "))

for i in range(0,len(prs)):
    prs = prs.replace(" ","")

prs = prs.lower()

prs = list(prs)

prs.sort()

rst = ""

for i in range(0,len(prs)):
    rst += prs[i]

print(rst)
