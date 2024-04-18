"""i = 0
j = 10
n = 0
while i < j:
    i = i + 1
    j = j - 1
    n = n + 1
    print(i)
i = 0
j = 0
n = 0
while i < 10:
    i = i + 1
    n = n + i + j
    j = j + 1
    print(i)
a = 10
while a > 0:

    a = a - 1
    print(a)
x = int(input('Digite o valor final do conjunto:'))
comeco = int(input('Digite o valor incial do conjunto: '))
a = 1
while a <= x:
    if a % 2 == 1:
        print(f'{a} é impar')
    else:
        print(f'{a} é par')
        a = a + 1

a = int(input("Digite seu numero: "))
while True:
    a = int(input("Digite seu numero: 22 "))
    if a == 0:
        break
print("Fim do programa")

i = 0
soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 0:
        break
    i = i + 1
    soma = soma + n

print('Fim da execução:')
print(f'Quantidade de valores digitados: {i} ')
print(f'A soma dos valores: {soma}')
print(f'A media é {soma/i:.2f}')
"""
while True:
    cod = int(input('Digite o codigo do produto: '))
    qtd = int(input('Digite a qtde desejada:'))
    
