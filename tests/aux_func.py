import requests

ENDPOINT = "https://compassuol.serverest.dev"
EMAIL = "email@teste.com"


"""
FUNÇÕES AUXILIARES
"""


def register():

    payload = {
        "nome": "Fulano da Silva GENERICO",
        "email": EMAIL,
        "password": "teste123",
        "administrador": "true"
    }

    response = requests.post(
        ENDPOINT + "/usuarios",
        json=payload
    )

    return response


def login(email, password="teste123"):
    payload = {
        "email": email,
        "password": password
    }

    return requests.post(
        ENDPOINT + "/login",
        json=payload
    )


def get_users():
    return requests.get(ENDPOINT + "/usuarios")


def get_user_by_id(user_id):
    return requests.get(
        ENDPOINT + f"/usuarios/{user_id}"
    )


def update_user(user_id, email):
    payload = {
        "nome": "Usuario Atualizado",
        "email": email,
        "password": "novaSenha123",
        "administrador": "true"
    }

    return requests.put(
        ENDPOINT + f"/usuarios/{user_id}",
        json=payload
    )


def delete_user(user_id):
    return requests.delete(
        ENDPOINT + f"/usuarios/{user_id}"
    )

# =========================
# PRODUTOS
# =========================

UPDATED_PRODUCT_NAME = "Produto Atualizado"

def get_admin_token():
    response = login(EMAIL)

    return response.json()["authorization"]

def get_headers():
    token = get_admin_token()

    return {
        "Authorization": token
    }


def create_product():
    payload = {
        "nome": "Produto Teste",
        "preco": 100,
        "descricao": "Descricao Produto Teste",
        "quantidade": 10
    }

    return requests.post(
        ENDPOINT + "/produtos",
        json=payload,
        headers=get_headers()
    )


def create_product_without_token():
    payload = {
        "nome": "Produto Sem Token",
        "preco": 100,
        "descricao": "Descricao",
        "quantidade": 10
    }

    return requests.post(
        ENDPOINT + "/produtos",
        json=payload
    )


def list_products():
    return requests.get(
        ENDPOINT + "/produtos"
    )


def get_product_by_id(product_id):
    return requests.get(
        ENDPOINT + f"/produtos/{product_id}"
    )


def update_product(product_id):
    payload = {
        "nome": UPDATED_PRODUCT_NAME,
        "preco": 150,
        "descricao": "Descricao Atualizada",
        "quantidade": 20
    }

    return requests.put(
        ENDPOINT + f"/produtos/{product_id}",
        json=payload,
        headers=get_headers()
    )


def delete_product(product_id):
    return requests.delete(
        ENDPOINT + f"/produtos/{product_id}",
        headers=get_headers()
    )