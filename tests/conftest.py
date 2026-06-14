import pytest
from aux_func import *


@pytest.fixture
def user():
    response = register()

    assert response.status_code == 201, response.text

    user_id = response.json()["_id"]

    yield user_id

    delete_user(user_id)


@pytest.fixture
def auth_token():
    response = register()

    assert response.status_code == 201, response.text

    user_id = response.json()["_id"]
    email = response.used_email

    token_response = login(email)

    assert token_response.status_code == 200, token_response.text

    yield token_response.json()["authorization"]

    delete_user(user_id)


@pytest.fixture
def produto_criado(auth_token):
    response = create_product(auth_token)

    assert response.status_code == 201, response.text

    product_id = response.json()["_id"]

    yield product_id

    delete_product(product_id, auth_token)