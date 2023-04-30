import pytest
import requests
from pydantic import BaseModel


class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_needed():
    request = {
        "access_token": "test_token"
    }
    AccessTokenRequest(**request)


def test_users_receives_response():
    response = [
        {"id": 101010, "first_name": "Anastasia", "last_name": "Tsytsartseva"},
        {"id": 010101, "first_name": "Ivan", "last_name": "Dorn"}
    ]
    users = [User(**user) for user in response]



def test_access_token_needed():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_users_succeed():
    response = [
        {"id": 101010, "first_name": "Anastasia", "last_name": "Tsytsartseva"},
        {"id": 010101, "first_name": "Ivan", "last_name": "Dorn"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 101010
    assert users[0].first_name == "Anastasia"
    assert users[0].last_name == "Tsytsartseva"


def test_users_don't_get_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Anastasia",
        "last_name": "Tsytsartseva"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_nameformat():
    user = {
        "id": 101010,
        "first_name": "Zina",
        "last_name": "Tsytsartseva"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_lastnameformat():
    user = {
        "id": 101010,
        "first_name": "Anastasia",
        "last_name": "Unknown"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_users_get_user():
    response = [{"id": 101010, "first_name": "Anastasia", "last_name": Tsytsartseva"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 101010
    assert users[0].first_name == "Anastasia"
    assert users[0].last_name == "Tsytsartseva"



def test_users_get_maxusers():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1000)
]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[-1].id == 999
    assert users[-1].first_name == "User"
    assert users[-1].last_name == "999"


def test_users_get_incorrect_response():
    response = [{"invalid_attr": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]
