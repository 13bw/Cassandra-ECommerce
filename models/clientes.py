from cassandra_db import get_cassandra_session

def cadastrar_cliente(cliente_id, nome, endereco, email):
    session = get_cassandra_session()
    query = "INSERT INTO Clientes (cliente_id, nome, endereco, email) VALUES (%s, %s, %s, %s)"
    session.execute(query, (cliente_id, nome, endereco, email))

def buscar_pedidos_por_cliente(cliente_id):
    session = get_cassandra_session()
    query = "SELECT * FROM PedidoItens WHERE cliente_id = %s"
    return session.execute(query, (cliente_id,))

