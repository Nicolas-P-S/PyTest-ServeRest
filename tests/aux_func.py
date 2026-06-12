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

