# Utilizar lambda em uma função anônima
contador_letras = lambda lista:[len(x) for x in lista]

# É a mesma coisa que o codigo abaixo:

# def contador_letras(lista_letras):
#     contador = []
#     for x in lista_letras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

lista_animais = ('cachorro', 'gato', 'elefante')
print(contador_letras(lista_animais))

# Calculadora em lambda
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(5,10))
print(subtracao(10,4))
print(multiplicacao(5,5))
print(divisao(10,2))

# Calculadora em dicionario lambda *** COM VIRGULA NO FINAL ***
calculadora = {
    'soma': lambda a,b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma_ = calculadora['soma']
subtracao_ = calculadora['subtracao']
multiplicacao_ = calculadora['multiplicacao']
divisao_ = calculadora['divisao']

print('A soma em dicionário é: {}'.format(soma_(70,8)))
print('A subtracao em dicionário é: {}'.format(subtracao_(30,15)))
print('A multiplicacao em dicionário é: {}'.format(multiplicacao_(3,8)))
print('A divisao em dicionário é: {}'.format(divisao_(70,10)))
