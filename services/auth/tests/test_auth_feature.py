from pytest_bdd import given, when, then, scenario, parsers

import jwt


@scenario(
    "../features/auth.feature",
    "The system can generate a valid authentication token",
)
def test_token_creation():
    pass


@scenario(
    "../features/auth.feature",
    "The system can validate an authentication token",
)
def test_token_validation():
    pass


@given(parsers.parse("user id {user_id:d}"))
def user_id(user_id):
    assert isinstance(user_id, int)


@given(parsers.parse("user role {user_role:d}"))
def user_role(user_role):
    assert isinstance(user_role, int)


@given(parsers.parse("secret key {secret_key}"))
def secret_key(secret_key):
    assert isinstance(secret_key, str)


@when("generating an auth token", target_fixture="generated_access_token")
def generate_auth_token(auth, secret_key, user_id, user_role):
    generated_access_token = auth.create_access_token(user_id, user_role, secret_key)
    return generated_access_token


@then(parsers.parse("the auth token is {auth_token}"))
def resulting_auth_token(generated_access_token, auth_token, auth_tokens):
    assert generated_access_token == auth_tokens[auth_token]


@given(parsers.parse("an auth token {auth_token}"))
def auth_token(auth_token):
    assert isinstance(auth_token, str)


@when("validating the auth token", target_fixture="decoded_token_result")
def validate_token(auth, auth_token, auth_tokens):
    decoded_token = auth.decode_access_token(auth_tokens[auth_token])
    return decoded_token


@then(parsers.parse("the decoded token is {decoded_token}"))
def decoded_token(decoded_auth_tokens, decoded_token, decoded_token_result):
    assert type(decoded_auth_tokens[decoded_token]) == type(decoded_token_result)
