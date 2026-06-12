import requests
from aux_func import *

"""
TESTES
"""


def test_endpoint_call_200():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200


def test_list_users_should_return_200():
    response = get_users()

    assert response.status_code == 200

    data = response.json()

    assert "usuarios" in data
    assert isinstance(data["usuarios"], list)


def test_register_valid_user_should_return_201():
    response = register()

    assert response.status_code == 201

    data = response.json()

    assert "_id" in data
    assert data["message"] == "Cadastro realizado com sucesso"

    delete_user(data["_id"])


def test_get_user_by_valid_id_should_return_200():
    register_response = register()

    assert register_response.status_code == 201

    user_id = register_response.json()["_id"]

    response = get_user_by_id(user_id)

    assert response.status_code == 200

    data = response.json()

    assert data["_id"] == user_id
    assert data["email"] == EMAIL

    delete_user(user_id)


def test_get_user_by_invalid_id_should_return_400():
    response = get_user_by_id(
        "idInexistente123"
    )

    assert response.status_code == 400


def test_update_user_should_return_200():
    register_response = register()

    assert register_response.status_code == 201

    user_id = register_response.json()["_id"]

    new_email = EMAIL

    response = update_user(
        user_id,
        new_email
    )

    assert response.status_code == 200

    get_response = get_user_by_id(user_id)

    assert get_response.status_code == 200 or get_response.status_code == 201
    assert (
        get_response.json()["email"]
        == new_email
    )

    delete_user(user_id)


def test_delete_user_should_return_200():
    register_response = register()

    assert register_response.status_code == 201

    user_id = register_response.json()["_id"]

    response = delete_user(user_id)

    assert response.status_code == 200


def test_delete_invalid_user_should_return_200():
    response = delete_user(
        "idInexistente123"
    )

    assert response.status_code == 200