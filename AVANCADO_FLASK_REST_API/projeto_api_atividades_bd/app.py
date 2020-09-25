from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

from models import Pessoas, Atividades, Usuarios

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# usuarios = {
#     'rogerio':'123',
#     'larissa': '321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     print('Validando Usuarios')
#     print(usuarios.get(login) == senha)
#     if not (login, senha):
#         return False
#     return usuarios.get(login) == senha

# Função de Solicitação de login
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()
    return "Olá, {}!".format(auth.current_user())

########################
class Pessoa(Resource):
# Solicitando o login
    @auth.login_required
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada',
            }
        return response

    def put(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dados = request.json
            # Só alterar apenas nome e idade)
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
                pessoa.save()
                response = {
                    'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade
                }
        except AttributeError:
            response = {
            'status': 'error',
            'mensagem': 'Pessoa não encontrada',
            }
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = { 'ID excluido'}
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

##########################
class Lista_Pessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

# *******************

class Atividade(Resource):
    def get(self, pessoa):
        pessoa = Pessoas.query.filter_by(nome=pessoa).first()
        response = [{'id': pessoa.id, 'nome': pessoa.nome} for i in atividades]
        return response


    def put(self, nome):
        try:
            atividade = Atividades.query.filter_by(nome=nome).first()
            dados = request.json
            # Só alterar apenas nome e idade)
            atividade.idade = dados['idade']
            atividade.save()
            response = {
                'id': atividade.id,
                'nome': atividade.nome,
            }
        except AttributeError:
            response = {
            'status': 'error',
            'mensagem': 'Pessoa não encontrada',
            }
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = { 'ID excluido'}
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

class Lista_Atividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id,'nome': i.nome,'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoas/<string:nome>/')
api.add_resource(Lista_Pessoas, '/pessoas/')
api.add_resource(Atividade, '/atividades/<string:pessoa>/')
api.add_resource(Lista_Atividades, '/atividades/')



if __name__ == '__main__':
    app.run(debug=True)
