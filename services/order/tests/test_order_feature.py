from pytest_bdd import given, when, then, scenario, parsers


@scenario(
    "order.feature",
    "The system can calculate the inventory",
    features_base_dir="./features",
)
def test_calculate_inventory():
    pass


@given(parsers.parse("a quantity {quantity:d}"))
def quantity(quantity):
    assert isinstance(quantity, int)


@given(parsers.parse("a product id {product_id:d}"))
def product_id(product_id):
    assert isinstance(product_id, int)


@when("calculating the remaining inventory", target_fixture="new_inventory")
def calculate_new_inventory(order, quantity, product_id, products):
    product_inventory = products[product_id]["inventory"]
    order.quantity = quantity
    new_inventory = order.calculate_new_inventory(product_inventory)
    return new_inventory


@then(parsers.parse("the result is {expected_result:d}"))
def result(expected_result, new_inventory):
    assert new_inventory == expected_result
