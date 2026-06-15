from aux_func import *

def test_get_listar_produtos():
    response = get_products()
    data = response.json()

    assert response.status_code == 200
    assert "produtos" in data
    assert "quantidade" in data
    assert isinstance(data["produtos"], list)

def test_post_cria_produto(produto_criado):
    assert produto_criado is not None
    assert isinstance(produto_criado, str)

def test_post_cria_produto_in_3_sec(auth_token):
    inicio = time.time()

    response = create_product(auth_token)
    data = response.json()

    fim  = time.time()
    tempo = fim-inicio

    assert tempo < 3, f"Criação de produto demorou {tempo:.2f}s (esperado menor que 3s)"
    delete_product(data["_id"], auth_token)




def test_post_cria_produto_repetido(auth_token):
    responseOriginal = create_product(auth_token)
    responseRepetido = create_product(auth_token)
    dataOriginal = responseOriginal.json()
    dataRepetido = responseRepetido.json()

    assert responseRepetido.status_code == 400
    assert dataRepetido["message"] == "Já existe produto com esse nome"

    delete_product(dataOriginal["_id"], auth_token)


def test_post_cria_produto_token_ausente():
    response = create_product("TOKEN_INCORRETO")
    data = response.json()

    assert response.status_code == 401
    assert data["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

def test_get_produto_por_id(produto_criado):
    response = get_product_by_id(produto_criado)
    data = response.json()

    assert response.status_code == 200
    assert "_id" in data
    assert data["_id"] == produto_criado


def test_get_produto_por_id_inexistente():
    response = get_product_by_id("idInexistente123")
    data = response.json()

    assert response.status_code == 400
    assert data["message"] == "Produto não encontrado"

def test_delete_produto(produto_criado, auth_token):
    response = delete_product(produto_criado, auth_token)
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "Registro excluído com sucesso"


def test_delete_produto_inexistente(auth_token):
    response = delete_product("idInexistente123", auth_token)
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "Nenhum registro excluído"


def test_delete_produto_token_ausente(produto_criado):
    response = delete_product(produto_criado, "TOKEN_INCORRETO")
    data = response.json()

    assert response.status_code == 401
    assert data["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

def test_put_atualiza_produto(produto_criado, auth_token):
    response = update_product(produto_criado, auth_token)
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "Registro alterado com sucesso"


def test_put_produto_inexistente(auth_token):
    response = update_product("idInexistente123", auth_token)
    data = response.json()

    assert response.status_code == 201
    assert data["message"] == "Cadastro realizado com sucesso"
    assert "_id" in data

    delete_product(data["_id"], auth_token)


def test_put_produto_token_ausente(produto_criado):
    response = update_product(produto_criado, "TOKEN_INCORRETO")
    data = response.json()

    assert response.status_code == 401
    assert data["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"