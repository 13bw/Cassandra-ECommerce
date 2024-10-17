from cassandra_db import get_cassandra_session

def realizar_pedido_db(pedido_id, produto_id, quantidade, preco_unitario):
    session = get_cassandra_session()
    query = "INSERT INTO PedidoItens (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
    session.execute(query, (pedido_id, produto_id, quantidade, preco_unitario))

def buscar_itens_por_pedido(pedido_id):
    session = get_cassandra_session()
    query = "SELECT * FROM PedidoItens WHERE pedido_id = %s"
    return session.execute(query, (pedido_id,))
