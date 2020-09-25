from models import Programadores, Habilidades, Programadores_Habilidades

# ************* Funções da classe Programadores *************************
def inserir_programador():
    programador = Programadores(nome="Gilmar", idade=45, email="juma@gmail.com")
    programador.save()
    print(programador)

def consultar_programadores():
    programador = Programadores.query.all()
    print(programador)

def consultar_um_programador():
    programador = Programadores.query.filter_by(nome='Rogerio').first()
    print('Nome: {}\nIdade: {}'.format(programador.nome,programador.idade))

def alterar_programador():
    programador = Programadores.query.filter_by(nome='Rogerio').first()
    programador.idade = 20
    programador.save()

def excluir_programador():
    programador = Programadores.query.filter_by(nome='Galeane').first()
    programador.delete()

# ************* Funções da classe Habilidades *************************
def inserir_habilidade():
    habilidade = Habilidades(nome="C#")
    habilidade.save()
    print(habilidade)


def consultar_habilidades():
    habilidade = Habilidades.query.all()
    print(habilidade)

def consultar_uma_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Java').first()
    print('Nome: {}'.format(habilidade.nome))

def alterar_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Java').first()
    habilidade.nome = "SAP"
    habilidade.save()

def excluir_habilidade():
    habilidade = Habilidades.query.filter_by(nome='SAP').first()
    habilidade.delete()

# ************* Funções da classe Programadores Habilidades *************************
def inserir_programador_habilidade():
    programador_habilidade = Programadores_Habilidades(programador='Larissa', habilidade='SAP')
    programador_habilidade.save()
    print(programador_habilidade)

def alterar_programador_habilidade():
    programador_habilidade = Programadores_Habilidades.query.filter_by(nome='Java').first()
    programador_habilidade.id = 1
    programador_habilidade.save()

def excluir_programador_habilidade():
    programador_habilidade = Programadores_Habilidades.query.filter_by(nome='SAP').first()
    programador_habilidade.delete()

def consultar_programadores_habilidade():
    programador_habilidade = Programadores_Habilidades.query.all()
    print(programador_habilidade)

def consultar_um_programador_habilidade():
    programador_habilidade = Programadores_Habilidades.query.filter_by(id=2).first()
    print('ID: {}'.format(programador_habilidade.programador))



if __name__ == '__main__':
    # ******* Chamar Funções Programador
    #inserir_programador()
    #consultar_programadores()
    #alterar_programador()
    #consultar_um_programador()
    #excluir_programador()
    #consultar_programadores()

    # ******* Chamar Funções Habilidades
    #inserir_habilidade()
    #consultar_habilidades()
    #consultar_uma_habilidade()
    #alterar_habilidade()
    #excluir_habilidade()
    #consultar_habilidades()

    # ******* Funções Programador
    #consultar_programadores_habilidade()
    inserir_programador_habilidade()