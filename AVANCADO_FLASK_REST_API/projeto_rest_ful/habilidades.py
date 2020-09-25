import json
from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

lista_habilidades = [
    {
        'id':0,''
               'habilidades': ['Java', 'Salesforce']},
    {'id':1,
     'habilidades': ['Fluter','Ionic']},
    {'id':2,'habilidades': ['Python','Django']}]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]

class Habilidade(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
            # Tratar erro de indexação, registro não existe
        except IndexError:
            mensagem = 'A habilidade de ID {} não existe na lista'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
            # Tratar erro geral
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}


