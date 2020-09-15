lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal)
print(lista_animal[2])
print('Animal nº 2: {}'.format(lista_animal[2]))

# Listar os animais da lista
for x in lista_animal:
    print(x)

# Somar a lista
print('A soma dessa lista é: {}'.format(sum(lista)))

# Menor valor da lista
print('O maior valor dessa lista é: {}'.format(max(lista_animal)))

# Maior valor da lista
print('O menor valor dessa lista é: {}'.format(min(lista_animal)))

# Verificar a existencia de um elemento na lista
if 'lobo' in lista_animal:
    print('Existe')
else:
    print('Não existe')

# Multiplicar a lista
nova_lista = lista_animal * 3
print(nova_lista)

# Incluir elemento no final
print(lista_animal.append('lobo'))
print(lista_animal)

# Incluir elemento no final
print(lista_animal.insert(0,'capivara'))
print(lista_animal)

# Excluir elemento no final
print(lista_animal.pop())
print(lista_animal)

# Excluir elemento pela posição
print(lista_animal.pop(0))
print(lista_animal)

# Excluir pelo nome
lista_animal.remove('elefante')
print(lista_animal)

# Ordenar lista
lista_nova = [10, 30, 5, 7]
lista_animal_nova = ['lobo','arara','cachorro', 'gato', 'elefante']
lista_nova.sort()
lista_animal_nova.sort()
print(lista_nova)
print(lista_animal_nova)

# Reverter em ordem decrescente
lista_nova.reverse()
lista_animal_nova.reverse()
print(lista_nova)
print(lista_animal_nova)

# ----------------------------

# Tuplas são imutáveis
tupla = (1, 10, 12, 14)
print(tupla)

# Acesso ao elemento
print(tupla[0])

# Contador de elementos
print(len(tupla))

# Converter lista em tupla
tupla_animal = tuple(lista_animal_nova)
print(type(tupla_animal))
print(tupla_animal)

# Converter tupla em lista
lista_de_tupla = list(tupla_animal)
print(type(lista_de_tupla))
print(lista_de_tupla)










