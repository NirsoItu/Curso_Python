# Conjunto é feito em chaves, do tipo Set, não permite duplicidade
conjunto = {1, 2, 3, 4}
print(conjunto)

# Inserir elemento no conjunto
conjunto.add(5)
print(conjunto)

# Excluir elemento no conjunto
conjunto.discard(3)
print(conjunto)

# União de conjuntos sem duplicar
conjunto1 = {1, 2, 3, 4, 5, 10 }
conjunto2 = {5, 6, 7, 8, 9}
conjunto_unido = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_unido))

# Intersecção de conjuntos, mostra somente os repetidos
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

# Diference mostra somente os elementos diferentes de ambos conjuntos
conjunto_diferente1 = conjunto1.difference(conjunto2)
conjunto_diferente2 = conjunto2.difference(conjunto1)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferente1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferente2))

# Diferença simetrica mostra um conjunto dos valores que não se repetem
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simetrica entre 1 e 2: {}'.format(diferenca_simetrica))

# Subset retorna se um conjunto é um subconjunto de outro retornando um booleano
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Conjunto A é um subconjunto de Conjunto B ? {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('Conjunto B é um subconjunto de Conjunto A ? {}'.format(conjunto_subset))

# Superset retorna se um conjunto é um superset de outro retornando um booleano
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4}
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Conjunto B é um superset de Conjunto A ? {}'.format(conjunto_superset))

# Converter lista para conjunto para tirar a duplicidade
lista_a = ['arara','cachorro','gato','cachorro','cachorro','elefante']
conjunto_lista = set(lista_a)
print(conjunto_lista)

# Converter conjunto para lista
lista_b = list(conjunto_lista)
print(lista_b)

