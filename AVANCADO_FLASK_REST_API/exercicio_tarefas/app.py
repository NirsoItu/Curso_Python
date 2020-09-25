from flask import Flask, request, jsonify, json
app = Flask(__name__)


tarefas = [
    {'id':'0',
        'responsavel':'Rogerio',
      'tarefas':['Cortar o cabelo','Lavar o banheiro'],
    'status':'pendente'},
    {'id':'1',
        'responsavel':'Larissa',
      'tarefas':['Lavar a louca','Dar banho no cachorro'],
    'status':'concluido'}
]

@app.route("/task/<int:id>/", methods=['GET','PUT','DELETE''POST'])
def responsavel(id):
    # Devolve um desenvolvedor pelo ID
    if request.method == 'GET':
        try:
            response = tarefas[id]
            # Tratar erro de indexação, registro não existe
        except IndexError:
            mensagem = 'Responsável pela tarefa de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem': mensagem}
            # Tratar erro desconhecido
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    # Editar um desenvolvedor pelo ID
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    # Excluir um desenvolvedor pelo ID
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return ({'status':'sucesso', 'mensagem':'Excluído com sucesso'})

# Lista todas as tarefas
@app.route('/task/', methods=['GET','POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)