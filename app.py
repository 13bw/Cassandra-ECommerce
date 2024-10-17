from flask import Flask, jsonify,request
from models.clientes import cadastrar_cliente, buscar_pedidos_por_cliente
from cassandra_db import get_cassandra_session
from models.produtos import cadastrar_produto, buscar_produtos_por_categoria
from models.pedidos import realizar_pedido_db, buscar_itens_por_pedido

app = Flask(__name__)

@app.route('/cadastro_cliente', methods=['POST'])
def cadastro_cliente():
    try:
        data = request.get_json()  
        cliente_id = data['cliente_id']
        nome = data['nome']
        endereco = data['endereco']
        email = data['email']

        
        cadastrar_cliente(cliente_id, nome, endereco, email)
        return "Cliente cadastrado com sucesso!", 200

    except KeyError as e:
        return f"Erro: Chave {str(e)} não encontrada na requisição", 400

@app.route('/cadastro_produto', methods=['POST'])
def cadastro_produto():
    
    if request.method == 'POST':
        
        produto_id = request.json.get('produto_id')  
        nome = request.json.get('nome')
        preco = request.json.get('preco')
        categoria_id = request.json.get('categoria_id')

        
        cadastrar_produto(produto_id, nome, preco, categoria_id)

        
        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

    
    return jsonify({"message": "Método não permitido."}), 405


@app.route('/realizar_pedido', methods=['POST'])
def realizar_pedido():
    
    pedido_id = request.json.get('pedido_id')
    produto_id = request.json.get('produto_id')
    quantidade = request.json.get('quantidade')
    preco_unitario = request.json.get('preco_unitario')
    
    
    realizar_pedido_db(pedido_id, produto_id, quantidade, preco_unitario)

    
    return jsonify({"message": "Pedido realizado com sucesso!"}), 201


@app.route('/consultar_itens_pedido/<pedido_id>', methods=['GET'])
def consultar_itens_pedido(pedido_id):
    itens = buscar_itens_por_pedido(int(pedido_id))  
    
    
    itens_lista = []
    for item in itens:
        itens_lista.append({
            "produto_id": item.produto_id,
            "quantidade": item.quantidade,
            "preco_unitario": item.preco_unitario
        })
    
    if itens_lista:  
        return jsonify(itens_lista), 200  
    else:
        return jsonify({"message": "Nenhum item encontrado para este pedido."}), 404  

@app.route('/produtos_categoria/<categoria_id>', methods=['GET'])
def produtos_categoria(categoria_id):
    produtos = buscar_produtos_por_categoria(categoria_id)  
    
    
    produtos_lista = []
    for produto in produtos:
        produtos_lista.append({
            "produto_id": produto.produto_id,
            "nome": produto.nome,
            "preco": produto.preco,
            "categoria_id": produto.categoria_id
        })
    
    if produtos_lista:  
        return jsonify(produtos_lista), 200  
    else:
        return jsonify({"message": "Nenhum produto encontrado para esta categoria."}), 404  

def calcular_vendas_produto(produto_id):
    session = get_cassandra_session()
    query = "SELECT SUM(quantidade) AS total_vendas FROM PedidoItens WHERE produto_id = %s ALLOW FILTERING" 
    result = session.execute(query, (produto_id,))
    return result.one().total_vendas

def busca_produto_por_id(produto_id):
    session = get_cassandra_session()
    query = "SELECT * FROM ProdutosCategoria WHERE produto_id = %s ALLOW FILTERING"
    return session.execute(query, (produto_id,)).one()
@app.route('/total_vendas/<produto_id>')
def total_vendas(produto_id):
    total = calcular_vendas_produto(int(produto_id))
    produto_nome = busca_produto_por_id(int(produto_id)).nome
    return {
        'total_vendas': total,
        'nome_produto': produto_nome,
        'id_produto': produto_id
    }


if __name__ == '__main__':
    app.run(debug=True)