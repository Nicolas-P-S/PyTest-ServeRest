import requests
import time

ENDPOINT = "https://compassuol.serverest.dev"

EMAIL = f"test_{int(time.time())}@qa.com"

def generate_email():
    return f"test_{int(time.time() * 1000)}@qa.com"


def  register(email=None):
    if email is None:
        email = generate_email()

    payload = {
        "nome": "Fulano da Silva GENERICO",
        "email": email,
        "password": "teste123",
        "administrador": "true"
    }

    response = requests.post(
        ENDPOINT + "/usuarios",
        json=payload
    )
    response.used_email = email
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

def get_products():
    return requests.get(ENDPOINT+ "/produtos")

def create_product(token, payload=None):
    header = {"Authorization": token}

    if payload == None:
        payload = {
        "nome": "Produto generico TESTE2",
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
        }

    return requests.post(ENDPOINT+"/produtos", json=payload, headers=header)

def delete_product(id, token):
    header = {"Authorization": token}
    return requests.delete(ENDPOINT+"/produtos"+f"/{id}", headers=header)

def get_product_by_id(product_id):
    return requests.get(ENDPOINT + f"/produtos/{product_id}")


def update_product(product_id, token):
    header = {"Authorization": token}
    payload = {
        "nome": f"Produto Atualizado {int(time.time() * 1000)}",
        "preco": 500,
        "descricao": "Mouse Atualizado",
        "quantidade": 100
    }
    return requests.put(ENDPOINT + f"/produtos/{product_id}", json=payload, headers=header)
