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


televisao = Televisao()

print('Televisão está ligada ? {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada ? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))

print('Televisão está ligada ? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
televisao.aumetaCanal() # Aumenta o canal uma vez
televisao.aumetaCanal() # Aumenta o canal uma vez
print('Canal: {}'.format(televisao.canal))
televisao.diminuiCanal()
print('Canal: {}'.format(televisao.canal))
