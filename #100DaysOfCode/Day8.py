prs = str(input("Phrase: "))
prs_correct = []
response = ""


for i in range(0, len(prs)):
    if prs[i] != prs[i-1]:
        prs_correct.append(prs[i])
        response += prs[i]

print(response)
