from jsonschema import validate


schema_erro = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"}
    }
}

schema_produto = {
    "type": "object",
    "required": ["_id", "nome", "preco", "descricao", "quantidade"],
    "properties": {
        "_id":        {"type": "string"},
        "nome":       {"type": "string"},
        "preco":      {"type": "number"},
        "descricao":  {"type": "string"},
        "quantidade": {"type": "integer"}
    }
}

schema_lista_produtos = {
    "type": "object",
    "required": ["quantidade", "produtos"],
    "properties": {
        "quantidade": {"type": "integer"},
        "produtos": {
            "type": "array",
            "items": schema_produto
        }
    }
}

schema_produto_criado = {
    "type": "object",
    "required": ["message", "_id"],
    "properties": {
        "message": {"type": "string"},
        "_id":     {"type": "string"}
    }
}