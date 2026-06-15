from aux_func import *

def test_post_preco_negativo(auth_token):
    payload = {"nome": "Produto Preco Negativo", "preco": -1, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_preco_zero(auth_token):
    payload = {"nome": "Produto Preco Zero", "preco": 0, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_preco_string(auth_token):
    payload = {"nome": "Produto Preco String", "preco": "caro", "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)

def test_post_quantidade_negativa(auth_token):
    payload = {"nome": "Produto Qtd Negativa", "preco": 10, "descricao": "x", "quantidade": -1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_quantidade_zero(auth_token):
    payload = {"nome": "Produto Qtd Zero", "preco": 10, "descricao": "x", "quantidade": 0}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_quantidade_string(auth_token):
    payload = {"nome": "Produto Qtd String", "preco": 10, "descricao": "x", "quantidade": "muito"}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)

def test_post_nome_vazio(auth_token):
    payload = {"nome": "", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_nome_gigante(auth_token):
    payload = {"nome": "A" * 10000, "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_nome_caracteres_especiais(auth_token):
    payload = {"nome": "<script>alert(1)</script>", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)


def test_post_nome_apenas_espacos(auth_token):
    payload = {"nome": "     ", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)

def test_post_sem_nome(auth_token):
    payload = {"preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "nome" in data


def test_post_sem_preco(auth_token):
    payload = {"nome": "Produto Sem Preco", "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "preco" in data


def test_post_sem_descricao(auth_token):
    payload = {"nome": "Produto Sem Descricao", "preco": 10, "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "descricao" in data


def test_post_sem_quantidade(auth_token):
    payload = {"nome": "Produto Sem Quantidade", "preco": 10, "descricao": "x"}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "quantidade" in data


def test_post_body_vazio(auth_token):
    response = create_product(auth_token, {})

    assert response.status_code == 400

def test_post_campo_extra_ignorado(auth_token):
    payload = {
        "nome": f"Produto Campo Extra {int(time.time() * 1000)}",
        "preco": 10,
        "descricao": "x",
        "quantidade": 1,
        "campo_falso": "valor_falso"
    }
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 201

    if "_id" in data:
        delete_product(data["_id"], auth_token)

def test_post_sql_injection_nome(auth_token):
    payload = {"nome": "' OR '1'='1", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400

    if "_id" in data:
        delete_product(data["_id"], auth_token)