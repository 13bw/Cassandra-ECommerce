from cassandra.cluster import Cluster

def get_cassandra_session():
    cluster = Cluster(['localhost'])  
    session = cluster.connect()

    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS loja_virtual
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)

    session.set_keyspace('loja_virtual')

    session.execute("""
    CREATE TABLE IF NOT EXISTS ClientePedidos (
        cliente_id INT,
        pedido_id INT,
        data_pedido timestamp,
        total decimal,
        PRIMARY KEY (cliente_id, pedido_id)
    );
    """)

    session.execute("""
    CREATE TABLE IF NOT EXISTS ProdutosCategoria (
        produto_id INT,
        nome text,
        preco decimal,
        categoria_id text,
        PRIMARY KEY (categoria_id, produto_id)
    );
    """)

    session.execute("""
    CREATE TABLE IF NOT EXISTS PedidoItens (
        pedido_id INT,
        produto_id INT,
        quantidade int,
        preco_unitario decimal,
        PRIMARY KEY (pedido_id, produto_id)
    );
    """)

    session.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        cliente_id INT PRIMARY KEY,
        nome text,
        endereco text,
        email text
    );
    """)

    return session
