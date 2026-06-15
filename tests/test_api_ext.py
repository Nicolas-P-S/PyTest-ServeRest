from aux_func import *
import pytest

@pytest.mark.edge
def test_post_preco_negativo(auth_token):
    payload = {"nome": f"Produto Preco Negativo {int(time.time() * 1000)}", "preco": -1, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_preco_zero(auth_token):
    payload = {"nome": f"Produto Preco Zero {int(time.time() * 1000)}", "preco": 0, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_preco_string(auth_token):
    payload = {"nome": f"Produto Preco String {int(time.time() * 1000)}", "preco": "caro", "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_quantidade_negativa(auth_token):
    payload = {"nome": f"Produto Qtd Negativa {int(time.time() * 1000)}", "preco": 10, "descricao": "x", "quantidade": -1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_quantidade_zero(auth_token):
    payload = {"nome": f"Produto Qtd Zero {int(time.time() * 1000)}", "preco": 10, "descricao": "x", "quantidade": 0}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_quantidade_string(auth_token):
    payload = {"nome": f"Produto Qtd String {int(time.time() * 1000)}", "preco": 10, "descricao": "x", "quantidade": "muito"}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_nome_vazio(auth_token):
    payload = {"nome": "", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_nome_gigante(auth_token):
    payload = {"nome": "A" * 10000, "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_nome_caracteres_especiais(auth_token):
    payload = {"nome": f"<script>alert(1)</script> {int(time.time() * 1000)}", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_nome_apenas_espacos(auth_token):
    payload = {"nome": "     ", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400

@pytest.mark.edge
def test_post_sem_nome(auth_token):
    payload = {"preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "nome" in data

@pytest.mark.edge
def test_post_sem_preco(auth_token):
    payload = {"nome": f"Produto Sem Preco {int(time.time() * 1000)}", "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "preco" in data

@pytest.mark.edge
def test_post_sem_descricao(auth_token):
    payload = {"nome": f"Produto Sem Descricao {int(time.time() * 1000)}", "preco": 10, "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "descricao" in data

@pytest.mark.edge
def test_post_sem_quantidade(auth_token):
    payload = {"nome": f"Produto Sem Quantidade {int(time.time() * 1000)}", "preco": 10, "descricao": "x"}
    response = create_product(auth_token, payload)
    data = response.json()

    assert response.status_code == 400
    assert "quantidade" in data

@pytest.mark.edge
def test_post_body_vazio(auth_token):
    response = create_product(auth_token, {})

    assert response.status_code == 400

@pytest.mark.edge
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

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 201

@pytest.mark.edge
def test_post_sql_injection_nome(auth_token):
    payload = {"nome": f"' OR '1'='1 {int(time.time() * 1000)}", "preco": 10, "descricao": "x", "quantidade": 1}
    response = create_product(auth_token, payload)
    data = response.json()

    if "_id" in data:
        delete_product(data["_id"], auth_token)

    assert response.status_code == 400