from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome="Galeane", idade=50)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)

def consulta_pessoa_unica():
    pessoa = Pessoas.query.filter_by(nome='Rogerio').first()
    print('Nome: {}\nIdade: {}'.format(pessoa.nome,pessoa.idade))

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rogerio').first()
    pessoa.idade = 20
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galeane').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':

    #insere_usuario('rogerio','123')
    consulta_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #consulta_pessoa_unica()
    #exclui_pessoa()
    #consulta_pessoas()

