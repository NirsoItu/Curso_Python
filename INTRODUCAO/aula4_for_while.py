# For com Range

# ** Saber a quantidade de números primos **

# a = int(input('Digite um número: '))
# div = 0
#
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo: '.format(a))
# else:
#     print('Número {} não é primo: '.format(a))

# ------------------------------
# for num in range(101):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# ------------------------------

# While
# a = 0
#
# while a <= 10:
#     print(a)
#     a += 1

primeiro_Bi = int(input('Digite a nota do primero bimestre: '))
while primeiro_Bi > 10:
     primeiro_Bi = int(input('Você digitou o valor acima de 10 para o Primeiro Bismestre, tente novamente: '))

segundo_Bi = int(input('Digite a nota do segundo bimestre: '))
while segundo_Bi > 10:
    segundo_Bi = int(input('Você digitou o valor acima de 10 para o Segundo Bismestre, tente novamente: '))

terceiro_Bi = int(input('Digite a nota do terceiro bimestre: '))
while terceiro_Bi > 10:
        terceiro_Bi = int(input('Você digitou o valor acima de 10 para o Terceiro Bismestre, tente novamente: '))

quarto_Bi = int(input('Digite a nota do quarto bimestre: '))
while quarto_Bi > 10:
        quarto_Bi = int(input('Você digitou o valor acima de 10 para o Quarto Bismestre, tente novamente: '))

media = (primeiro_Bi + segundo_Bi + terceiro_Bi + quarto_Bi) / 4

print('Média: {}'.format(media))