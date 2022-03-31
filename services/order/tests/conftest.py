from pytest import fixture

from order import Order


@fixture
def order(quantity: int) -> Order:
    auth_token = ""
    product_id = 1
    yield Order(auth_token, product_id, quantity)


@fixture
def products() -> dict:
    products = {
        1: {"inventory": 7},
        2: {"inventory": 4},
    }
    return products
