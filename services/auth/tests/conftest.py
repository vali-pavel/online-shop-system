from pytest import fixture
import jwt

from ..auth import Auth


@fixture
def auth() -> Auth:
    yield Auth()


@fixture
def auth_tokens() -> dict:
    auth_tokens = {
        "AUTH-TOKEN1": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjAsInJvbGUiOjB9.SkQ_Vk1G7o9Bp3aPmtDyeaA5lxHUWA67V5lMNLsVe0o",
        "AUTH-TOKEN2": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsInJvbGUiOjF9.HEB-2dJxkjBDPIyUQexb0MTnHB7CVn7UgGhYzjQev9M",
        "BAD-AUTH-TOKEN1": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMsInJvbGUiOjB9.VUl1SxmhKzgQOJJ76n499tfoXZuwbAxvidCLHf1D14E",
    }
    return auth_tokens
