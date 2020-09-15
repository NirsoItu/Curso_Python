# Colocar as chamadas das funções no main
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumetaCanal(self):
        if self.ligada:
            self.canal += 1

    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':

    televisao = Televisao()
    print('Televisão está ligada ? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada ? {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
