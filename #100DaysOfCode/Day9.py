import os

prs = str(input("Frase: "))
os.system("cls")
convert = int(input("CamelCase [0] -=- snake_case [1]: "))
os.system("cls")

def getCamelCase (prs):
    prs = prs.title()
    prs = prs.replace(" ","")
    return prs

def get_snake_case (prs):
    prs = prs.lower()
    prs = prs.replace(" ","_")
    return prs

if convert == 0:
    prs = getCamelCase(prs)
    print(prs)

elif convert == 1:
    prs = get_snake_case(prs)
    print(prs)
