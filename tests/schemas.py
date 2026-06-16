from jsonschema import validate


schema_login_sucesso = {
    "type": "object",
    "required": ["message", "authorization"],
    "properties": {
        "message":       {"type": "string"},
        "authorization": {"type": "string"}
    }
}

schema_erro = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"}
    }
}

schema_usuario = {
    "type": "object",
    "required": ["nome", "email", "password", "administrador", "_id"],
    "properties": {
        "nome":          {"type": "string"},
        "email":         {"type": "string"},
        "password":      {"type": "string"},
        "administrador": {"type": "string", "enum": ["true", "false"]},
        "_id":           {"type": "string"}
    }
}

schema_lista_usuarios = {
    "type": "object",
    "required": ["quantidade", "usuarios"],
    "properties": {
        "quantidade": {"type": "integer"},
        "usuarios": {
            "type": "array",
            "items": schema_usuario
        }
    }
}

schema_usuario_criado = {
    "type": "object",
    "required": ["message", "_id"],
    "properties": {
        "message": {"type": "string"},
        "_id":     {"type": "string"}
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