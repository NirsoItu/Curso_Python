# Exercícios de condicionais

# EXERCÍCIO 1
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))
#     print('Final do programa')

# EXERCÍCIO 2
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0 :
#     print('Foi digitado um Número par')
# else:
#     print('Nenhum Número par foi digitado')

# EXERCÍCIO 3
primeiro_Bi = int(input('Digite a nota do primero bimestre: '))
if primeiro_Bi > 10:
    primeiro_Bi = int(input('Você digitou o valor acima de 10 para o Primeiro Bismestre, tente novamente: '))

segundo_Bi = int(input('Digite a nota do segundo bimestre: '))
if segundo_Bi > 10:
    segundo_Bi = int(input('Você digitou o valor acima de 10 para o Segundo Bismestre, tente novamente: '))

terceiro_Bi = int(input('Digite a nota do terceiro bimestre: '))
if terceiro_Bi > 10:
    terceiro_Bi = int(input('Você digitou o valor acima de 10 para o Terceiro Bismestre, tente novamente: '))

quarto_Bi = int(input('Digite a nota do quarto bimestre: '))
if quarto_Bi > 10:
    quarto_Bi = int(input('Você digitou o valor acima de 10 para o Quarto Bismestre, tente novamente: '))

media = (primeiro_Bi + segundo_Bi + terceiro_Bi + quarto_Bi) / 4

print('Média: {}'.format(media))




# if primeiro_Bi > 10 or segundo_Bi > 10 or terceiro_Bi > 10 or quarto_Bi > 10:
#     print('Erro alguma nota foi informada com valor acima de 10')
# else: print('Média: {}'.format(media))


