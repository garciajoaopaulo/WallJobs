from flask import request, jsonify
from app import app, db
from app.models import Produto

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.json
    novo_produto = Produto(nome_do_produto=data['nome_do_produto'],
                           codigo_do_produto=data['codigo_do_produto'],
                           descricao_do_produto=data['descricao_do_produto'],
                           preco_do_produto=data['preco_do_produto'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'message': 'Produto adicionado com sucesso!'}), 201

# Adicione aqui as rotas GET, PUT e DELETE