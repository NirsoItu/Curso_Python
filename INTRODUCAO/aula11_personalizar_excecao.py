# Criando uma classe de erro
class Error(Exception):
    pass

# Extender a classe de erro
class InputError(Error):
    def __init__(self, message):
        self.message = message

# Exceção personalizada que não aceita letras
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            # Forçando uma exception
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Digite somente números!')
    # Avisando sobre o erro personalizado
    except InputError as ex:
        print(ex)



