from flask import Flask, request, json_available, jsonify
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, Habilidade, lista_habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':0, 'nome':'Rogério', 'habilidades':['Java', 'Python']
    },
    {
        'id':1, 'nome':'Affonso', 'habilidades': ['C#', 'PHP']
    },
    {
        'id':2, 'nome':'Lemos', 'habilidades': ['Ionic', 'Flutter']
    },
]

# Classe com funções por id
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
            # Tratar erro de indexação, registro não existe
        except IndexError:
            mensagem = 'Desenvoledor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
            # Tratar erro geral
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

# Classe com a lista completa e função de adicionar
class Lista_Desenvolvedores(Resource):
    def get(self):
        qtd = len(desenvolvedores)
        if (qtd == 0):
            response = "Não existe fornecedores cadastrados"
            print("Não existe fornecedores cadastrados")
        else:
            response = desenvolvedores
            print(desenvolvedores)
        return response

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        habilidade_recebida = dados['habilidades']
        listagem_nomes = [d['habilidades'] for d in lista_habilidades]
        if habilidade_recebida in listagem_nomes:
            desenvolvedores.append(dados)
            response = 'Dados incluidos com sucesso'
            print('Dados incluidos com sucesso')
        else:
            response = 'Habilidade não existe na listagem'
            print('Habilidade não existe na listagem')

        return response

# Adicionando as rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/dev/habilidades/')
api.add_resource(Habilidade, '/dev/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)