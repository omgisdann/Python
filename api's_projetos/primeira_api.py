print('SISTEMA DE PRODUTOS ///  API')

from flask import Flask, jsonify, request

app = Flask (__name__)

produtos = [
            {'id':1, 'nome': 'arroz', 'preco': 15.00, 'qte': 99}, 
            {'id': 2, 'nome': 'feijão', 'preco': 8.00, 'qte': 99},
            {'id':3, 'nome': 'ervilha', 'preco': 5.00, 'qte': 99}
           ]

@app.route('/produtos', methods = ['GET'])
def visualizacao_de_todos_os_produtos():
    return jsonify(produtos)


@app.route('/produto_especifico/<int:id>', methods = ['GET'])
def produto_especifico(id):
   for produto in produtos:
        if produto['id'] == id:
            return jsonify(produto)
        else:
            return jsonify(produto)
       

@app.route('/cadastro', methods = ['POST'])
def cadastro_novo_produto():
    novos_dados = request.get_json(force=True) #recebendo informações do usuário!
    novo_dicionario = {}
    for produto in produtos:
        for chave,valor in produto.items():
            if chave == 'id':
                chaves_do_id = valor
    chaves_do_id +=1
    novo_dicionario = {'id': chaves_do_id,
                       'nome':novos_dados['nome'],
                       'preco': novos_dados['preco'],
                       'qte':novos_dados['qte']}
    produtos.append(novo_dicionario)
    return jsonify(produtos)


@app.route('/atualizar/<int:id>', methods = ['PUT'])
def atualizar (id):
    novo_valor = request.get_json(force=True)
    for produto in produtos:
        if produto['id'] == id:
            produto['qte'] = novo_valor['valor']
            return jsonify(produtos)
        else:
            return jsonify(produtos)
    


@app.route('/deletar/<int:id>', methods = ['DELETE'])
def deletar(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify(produtos)
        else:
            return jsonify(produtos)

app.run(port=5000, host='localhost', debug=True)