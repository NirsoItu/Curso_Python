# Acessando classes de outros arquivos
from aula8_modulos_televisao import Televisao
from aula8_modulo_calculadora import Calculadora

# Acessando somente a função de um arquivo
from aula8_modulo_contador_letras import contador_letras

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calculadora = Calculadora(10, 20)
print(calculadora.soma())

# Acessando função contador de letras
lista = ('arara', 'baleia', 'gato', 'rato')
total_de_letras = contador_letras(lista)
print('O total de letras da lista é: {}'.format(total_de_letras))