import pymongo

# Estabelecer conexão com o servidor MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Vivipizas"]

# Enum de status de funcionário
status_funcionario_enum = ["Indisponível", "Disponível"]

# Coleção Cliente
db.create_collection("Cliente", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nm_cliente", "cpf_cliente"],
        "properties": {
            "cp_id_cliente": {"bsonType": "objectId"},
            "nm_cliente": {"bsonType": "string", "maxLength": 100},
            "tel_cliente": {"bsonType": "string", "maxLength": 15},
            "endereco": {"bsonType": "string", "maxLength": 255},
            "cpf_cliente": {"bsonType": "string", "maxLength": 11},
            "qtd_compras": {"bsonType": "int", "minimum": 0},
            "categoria_cliente": {"bsonType": "string", "enum": ["bronze", "prata", "ouro"]}
        }
    }
})
db.Cliente.create_index([("cpf_cliente", pymongo.ASCENDING)], unique=True)

# Coleção Pedido
db.create_collection("Pedido", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["ce_cliente", "status_pedido"],
        "properties": {
            "cp_id_pedido": {"bsonType": "objectId"},
            "ce_cliente": {"bsonType": "objectId"},
            "data_pedido": {"bsonType": "date"},
            "observações": {"bsonType": "string", "maxLength": 255},
            "status_pedido": {"bsonType": "string", "enum": ["Não-confirmado", "Em aberto", "Concluído", "Cancelado"]},
            "valor_total": {"bsonType": "double", "minimum": 0}
        }
    }
})

# Coleção Cargo
db.create_collection("Cargo", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nm_cargo"],
        "properties": {
            "cp_id_cargo": {"bsonType": "objectId"},
            "nm_cargo": {"bsonType": "string", "maxLength": 100},
            "salario": {"bsonType": "double", "minimum": 0},
            "horas_semanais": {"bsonType": "int"}
        }
    }
})

# Coleção Funcionario
db.create_collection("Funcionario", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["ce_cargo", "nm_funcionario", "status_funcionario"],
        "properties": {
            "cp_id_funcionario": {"bsonType": "objectId"},
            "ce_cargo": {"bsonType": "objectId"},
            "nm_funcionario": {"bsonType": "string", "maxLength": 100},
            "cpf_funcionario": {"bsonType": "string", "maxLength": 11},
            "email_funcionario": {"bsonType": "string", "maxLength": 100},
            "tel_funcionario": {"bsonType": "string", "maxLength": 15},
            "tarefas_ativas": {"bsonType": "int", "minimum": 0},
            "status_funcionario": {"bsonType": "string", "enum": status_funcionario_enum}
        }
    }
})
db.Funcionario.create_index([("cpf_funcionario", pymongo.ASCENDING)], unique=True)

# Coleção Produto
db.create_collection("Produto", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["tipo_produto", "nm_produto", "preco_produto"],
        "properties": {
            "cp_id_produto": {"bsonType": "objectId"},
            "tipo_produto": {"bsonType": "string", "enum": ["pizza", "aperitivo", "sobremesa", "bebida", "bebida alcoolica", "utensilios"]},
            "nm_produto": {"bsonType": "string", "maxLength": 100},
            "preco_produto": {"bsonType": "double", "minimum": 0},
            "descricao": {"bsonType": "string", "maxLength": 255},
            "tamanho_pizza": {"bsonType": "string", "maxLength": 20},
            "volume_bebida": {"bsonType": "string", "maxLength": 20},
            "qtd_disponivel": {"bsonType": "int", "minimum": 0},
            "porcentagem_promoção": {"bsonType": "double", "maximum": 100}
        }
    }
})

# Coleção Ingrediente
db.create_collection("Ingrediente", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nm_ingrediente", "tipo"],
        "properties": {
            "cp_id_ingrediente": {"bsonType": "objectId"},
            "nm_ingrediente": {"bsonType": "string", "maxLength": 100},
            "tipo": {"bsonType": "string", "enum": ["animal", "vegetal", "farinha", "lacticinio", "outro"]}
        }
    }
})

# Coleção Funcionario_pedido
db.create_collection("Funcionario_pedido", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["ce_funcionario", "ce_pedido"],
        "properties": {
            "cp_id_pedido_id_funcionario": {"bsonType": "objectId"},
            "ce_funcionario": {"bsonType": "objectId"},
            "ce_pedido": {"bsonType": "objectId"},
            "papel": {"bsonType": "string", "maxLength": 50},
            "observação_funcionário": {"bsonType": "string", "maxLength": 100}
        }
    }
})

# Coleção Produto_pedido
db.create_collection("Produto_pedido", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["ce_produto", "ce_pedido", "qtd_compradas"],
        "properties": {
            "cp_id_pedido_id_produto": {"bsonType": "objectId"},
            "ce_produto": {"bsonType": "objectId"},
            "ce_pedido": {"bsonType": "objectId"},
            "qtd_compradas": {"bsonType": "int", "minimum": 1}
        }
    }
})

# Coleção Produto_ingrediente
db.create_collection("Produto_ingrediente", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["ce_produto", "ce_ingrediente"],
        "properties": {
            "cp_id_produto_id_ingrediente": {"bsonType": "objectId"},
            "ce_produto": {"bsonType": "objectId"},
            "ce_ingrediente": {"bsonType": "objectId"},
            "gramas_ingrediente": {"bsonType": "int", "minimum": 1}
        }
    }
})

print("Banco de dados MongoDB configurado com sucesso!")
