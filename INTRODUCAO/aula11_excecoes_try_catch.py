# Lançar o try except

lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[3]
    x = a

# Sempre colqque as exceções filhas antes do pai
except ZeroDivisionError:
    print('Não é possível fazer divisão por zero')
except IndexError:
    # Erro genérico
    print('Erro ao acessar um indice invalido na lista')

# Exemplo de exceção pai - genérica
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa se tudo der certo')

# Tudo que está no finally executa independente do except
finally:
    print('Sempre executa, independente da exceção aparecer ou não')