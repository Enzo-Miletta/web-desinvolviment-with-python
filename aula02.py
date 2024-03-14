"""
Comentários:
as palavras reservadas definem a sintaxe da linguagem e sua estrutura nao podem ser usadas como nomes de variavei
python tem pouco mais de trinta palavras reseravas:
and as assert break class continye def del elif else exept entre outras.
variavel = expressão
exemplo:
A=true
B= 5*4
C=A
D = B*A - 2>4
a atribuição é a operação que modifica o valor de suma variavel

bonus = 2500
penalizacao = 2500*5/100
bonusfinal = bonus - penalizacao
print ("Seu novo salário é de:", bonusfinal);"""
"""15var = fiap
R$ = 10000
class = engenharia"""
#primeiro caso
"""a = 10
a, b = 3*a, a
print("primeiro caso")
print (a, b)
a1 = 10
a1 = 3*a1
b1 = a1
print("Segundo caso")
print(a1, b1)
a = 10
b = 20
a = 2*a
b = b/2
print(a, b)
como professor faria:
a = 10
b = 20
temp = a
a = b
b = temp
print (a, b)
a = 2
b = 3
print( a==b )


segundos = 87426
dias = segundos // (24 * 3600)
horas = segundos // 3600
minutos = (segundos % 3600) // 60
print(segundos,"segundos equivalem a",dias,"dias, ou", horas, "horas e", minutos, "minutos")

a = 5
b = 5,5
print( a!=b )

--------------------------//---------------------"""

salario = 2000
idade = 99
flag_especial = 1

salario > 1500 and idade > 18
print((salario > 1500 and idade > 18 and idade <80) or flag_especial==1)
