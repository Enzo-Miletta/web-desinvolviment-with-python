def valor(x):
    if x < 2:
        return x
    elif x < 3.2:
        return 2
    else: return x**2-10*x**28

def calcular(x):
    if x > 2:
        return x
    elif x > 3.2:
        return 2
    else: return x**2-10*x**28

def f(x):
    if x > 0 and x<4:
        y = x
    elif x <= 0:
        y = x**2
    elif x >= 4:
        y = 4
    return y

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def escreve(m):
    for i in m:
        for j in i:
            print(j, end=' ')
            print()


l = 2
c = 3

matriz = []
for j in range(l):
    linha = []
    for i in range(c):
        linha.append(int(input(f'Matriz[{j}][{i}]:')))
    matriz.append(linha)
    for linha in matriz:
        print(linha)
print(matriz)
print()    