import requests
from schemas.user import post_create_user
from pytest_voluptuous import S

body_post_create_user = {
          "name": "morpheus",
          "job": "leader"
       }

credentials_for_registration = {
    "email": "eddddfvfvv@reqres.in",
    "password": "lic3423ka"
    }


def test_post_create_user_status_code():
    response = requests.post(url="https://reqres.in/api/users", json=body_post_create_user)

    assert response.status_code == 201


def test_post_create_user_has_name():
    response = requests.post(url="https://reqres.in/api/users", json=body_post_create_user)

    assert response.json().get('name')


def test_post_create_user_schema():
    response = requests.post(url="https://reqres.in/api/users", json=body_post_create_user)

    assert S(post_create_user) == response.json()


def test_registration_and_login():
    registration = requests.post(url="https://reqres.in/api/register", json=credentials_for_registration)
    login = requests.get(url="https://reqres.in/api/login", json=credentials_for_registration)

    assert login.status_code == 200
