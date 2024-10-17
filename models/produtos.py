from cassandra_db import get_cassandra_session

def cadastrar_produto(produto_id, nome, preco, categoria_id):
    session = get_cassandra_session()
    query = "INSERT INTO ProdutosCategoria (produto_id, nome, preco, categoria_id) VALUES (%s, %s, %s, %s)"
    session.execute(query, (produto_id, nome, preco, categoria_id))

def buscar_produtos_por_categoria(categoria_id):
    session = get_cassandra_session()
    query = "SELECT * FROM ProdutosCategoria WHERE categoria_id = %s"
    return session.execute(query, (categoria_id,))
