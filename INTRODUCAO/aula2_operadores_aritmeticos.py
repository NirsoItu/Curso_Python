# Operadores Aritméticos

a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# converter o inteiro para string usar a {} com .format

print('Soma: {}'.format(soma))
print('Subtracao: {}'.format(subtracao))
print('Multiplicação: {}'.format(multiplicacao))

# converter decimal em inteiro usar o 'int'
print('Divisão: {}'.format(int(divisao)))
print('Resto da divisão: {}'.format(resto))
print('\n-----------------\n')

# Tudo na mesma linha
print(f'Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}'
      f'\nDivisão: {divisao}\nResto: {resto}'
      .format(soma = soma, subtracao = subtracao,
              multiplicacao = multiplicacao, divisao = int(divisao),resto = resto))