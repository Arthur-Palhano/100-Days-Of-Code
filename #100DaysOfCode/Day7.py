def separate():
    print()
    print("-="*60)
    print()


c = int(input("Número de Colunas: "))
l = int(input("Número de Linhas: "))
op = str(input("Operação: "))
matriz1 = []

for i in range(0,l):
    matriz1.append([])

for i in range(l):
    for j in range(c):
        matriz1[i].append(int(input(f"Valor {i+1} X {j+1}: ")))

separate()

for i in range(l):
    print(matriz1[i])

separate()

matriz2 = []

for i in range(0,l):
    matriz2.append([])

for i in range(l):
    for j in range(c):
        matriz2[i].append(int(input(f"Valor {i+1} X {j+1}: ")))

separate()

for i in range(l):
    print(matriz2[i])

separate()

matrizResultante = []

for i in range(0,l):
    matrizResultante.append([])

for i in range(l):
    for j in range(c):
        if op == "+":
            matrizResultante[i].append(matriz1[i][j] + matriz2[i][j])
        elif op == "-":
            matrizResultante[i].append(matriz1[i][j] - matriz2[i][j])
        else:
            print("Operador não identificado")
for i in range(l):
    print(matrizResultante[i])
