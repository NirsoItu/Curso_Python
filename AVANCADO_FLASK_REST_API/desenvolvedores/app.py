from flask import Flask, request, jsonify, json
app = Flask(__name__)


desenvolvedores = [
    {'id':'0',
        'nome':'Rogerio',
      'habilidades':['Java','Ionic']},
    {'id':'1',
        'nome':'Rafael',
      'habilidades':['Python', 'JavaScript']}
]

@app.route("/dev/<int:id>/", methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    # Devolve um desenvolvedor pelo ID
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            # Tratar erro de indexação, registro não existe
        except IndexError:
            mensagem = 'Desenvoledor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem': mensagem}
            # Tratar erro desconhecido
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    # Editar um desenvolvedor pelo ID
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    # Excluir um desenvolvedor pelo ID
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return ({'status':'sucesso', 'mensagem':'Excluído com sucesso'})

# Lista de desenvolvedores
@app.route('/dev/', methods=['GET','POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
