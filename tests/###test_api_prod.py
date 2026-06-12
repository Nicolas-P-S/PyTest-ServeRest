import requests
from aux_func import *

"""
TESTES DE PRODUTOS
"""


def test_list_products_should_return_200():
    response = list_products()

    assert response.status_code == 200

    data = response.json()

    assert "produtos" in data
    assert isinstance(data["produtos"], list)


def test_create_product_should_return_201():
    response = create_product()

    assert response.status_code == 201

    data = response.json()

    assert "_id" in data
    assert data["message"] == "Cadastro realizado com sucesso"

    delete_product(data["_id"])


def test_get_product_by_valid_id_should_return_200():
    register_response = create_product()

    assert register_response.status_code == 201

    product_id = register_response.json()["_id"]

    response = get_product_by_id(product_id)

    assert response.status_code == 200

    data = response.json()

    assert data["_id"] == product_id
    assert "nome" in data
    assert "preco" in data
    assert "descricao" in data
    assert "quantidade" in data

    delete_product(product_id)


def test_get_product_by_invalid_id_should_return_400():
    response = get_product_by_id(
        "idInexistente123"
    )

    assert response.status_code == 400

    data = response.json()

    assert data["message"] == "Produto não encontrado"


def test_update_product_should_return_200():
    register_response = create_product()

    assert register_response.status_code == 201

    product_id = register_response.json()["_id"]

    response = update_product(product_id)

    assert response.status_code == 200

    data = response.json()

    assert (
        data["message"]
        == "Registro alterado com sucesso"
    )

    get_response = get_product_by_id(product_id)

    assert get_response.status_code == 200

    product = get_response.json()

    assert product["nome"] == UPDATED_PRODUCT_NAME
    assert product["preco"] == 150
    assert product["descricao"] == "Descricao Atualizada"
    assert product["quantidade"] == 20

    delete_product(product_id)


def test_delete_product_should_return_200():
    register_response = create_product()

    assert register_response.status_code == 201

    product_id = register_response.json()["_id"]

    response = delete_product(product_id)

    assert response.status_code == 200

    data = response.json()

    assert (
        data["message"]
        == "Registro excluído com sucesso"
    )


def test_delete_invalid_product_should_return_400():
    response = delete_product(
        "idInexistente123"
    )

    assert response.status_code == 400

    data = response.json()

    assert (
        data["message"]
        == "Produto não encontrado"
    )
