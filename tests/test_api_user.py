import requests
from aux_func import *

def test_endpoint_call_200():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200


# =========================
# USERS - LISTAGEM
# =========================

def test_list_users_should_return_200():
    response = get_users()

    assert response.status_code == 200

    data = response.json()

    assert "usuarios" in data
    assert isinstance(data["usuarios"], list)


# =========================
# USERS - LOGIN
# =========================

def test_login_valid_user_should_return_200():
    responseR = register()
    assert responseR.status_code == 201, responseR.text

    user_id = responseR.json()["_id"]
    email = responseR.used_email  # usa o email gerado neste registro

    response = login(email)

    assert response.status_code == 200, response.text

    data = response.json()

    assert data["message"] == "Login realizado com sucesso"
    assert data["authorization"].startswith("Bearer")

    delete_user(user_id)


def test_login_invalid_user_should_return_401():
    response = login("email_invalido@teste.com", "senha_errada")

    assert response.status_code == 401

    data = response.json()

    assert "message" in data
    assert "Email e/ou senha inválidos" in data["message"]

def test_login_without_email_should_return_400():
    payload = {"password": "teste123"}

    response = requests.post(ENDPOINT + "/login", json=payload)

    assert response.status_code == 400

    data = response.json()
    assert "email" in data


def test_login_without_password_should_return_400():
    payload = {"email": "qualquer@email.com"}

    response = requests.post(ENDPOINT + "/login", json=payload)

    assert response.status_code == 400

    data = response.json()
    assert "password" in data


# =========================
# USERS - CREATE
# =========================

def test_register_valid_user_should_return_201():
    response = register()

    assert response.status_code == 201

    data = response.json()

    assert "_id" in data
    assert data["message"] == "Cadastro realizado com sucesso"

    delete_user(data["_id"])


def test_register_duplicate_user_should_return_400():
    email = generate_email()  

    first = register(email)
    assert first.status_code == 201, first.text
    user_id = first.json()["_id"]

    response = register(email)  

    assert response.status_code == 400

    data = response.json()
    assert "message" in data

    delete_user(user_id)


# =========================
# USERS - GET BY ID
# =========================

def test_get_user_by_valid_id_should_return_200(user):
    response = get_user_by_id(user)

    assert response.status_code == 200

    data = response.json()

    assert data["_id"] == user


def test_get_user_by_invalid_id_should_return_400():
    response = get_user_by_id("idInexistente123")

    assert response.status_code == 400


# =========================
# USERS - UPDATE
# =========================

def test_update_user_should_return_200(user):
    new_email = generate_email()

    response = update_user(user, new_email)

    assert response.status_code == 200

    get_response = get_user_by_id(user)

    assert get_response.status_code == 200
    assert get_response.json()["email"] == new_email

# =========================
# USERS - DELETE
# =========================

def test_delete_user_should_return_200():
    response = register()

    assert response.status_code == 201, response.text

    user_id = response.json()["_id"]

    delete_response = delete_user(user_id)

    assert delete_response.status_code == 200


def test_delete_invalid_user_should_return_400():
    response = delete_user("idInexistente123")

    assert response.status_code == 200