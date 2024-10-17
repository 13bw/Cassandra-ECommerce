## E-Commerce Cassandra

### 1. Cadastro Cliente

**Endpoint**
```
http://localhost:5000/cadastro_cliente
```

**JSON**
```json
{
  "cliente_id": 1,
  "nome": "João Silva",
  "endereco": "Rua das Flores, 123",
  "email": "joao@email.com"
}
```

---

### 2. Cadastro Produto

**Endpoint**
```
http://localhost:5000/cadastro_produto
```

**JSON**
```json
{
  "produto_id": 1,
  "nome": "Smartphone",
  "preco": 1500.00,
  "categoria_id": "eletronicos"
}
```

---

### 3. Realização de Pedido

**Endpoint**
```
http://localhost:5000/realizar_pedido
```

**JSON**
```json
{
  "pedido_id": 1,
  "produto_id": 1,
  "quantidade": 12,
  "preco_unitario": 10
}
```


---

### 5. Consulta de Itens por Pedido

**Endpoint**
```
http://localhost:5000/consultar_itens_pedido/<pedido_id>
```

**JSON**
- **Parâmetro da URL**: `pedido_id` (ex: `1`)

**Resposta Exemplo**
```json
[
	{
		"preco_unitario": "10",
		"produto_id": 1,
		"quantidade": 12
	}
]
```

---

### 6. Consulta de Produtos por Categoria

**Endpoint**
```
http://localhost:5000/produtos_categoria/<categoria_id>
```

**JSON**
- **Parâmetro da URL**: `categoria_id` (ex: `categoria123`)

**Resposta Exemplo**
```json
[
	{
		"categoria_id": "eletronicos",
		"nome": "Smartphone",
		"preco": "1500.0",
		"produto_id": 1
	}
]
```

---

### 7. Consulta do Total de Vendas por Produto

**Endpoint**
```
http://localhost:5000/calcular_vendas/<produto_id>
```

**JSON**
- **Parâmetro da URL**: `produto_id` (ex: `1`)

**Resposta Exemplo**
```json
{
	"id_produto": "1",
	"nome_produto": "Smartphone",
	"total_vendas": 12
}
```

---
