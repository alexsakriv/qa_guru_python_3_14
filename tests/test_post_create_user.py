import requests
from pytest_voluptuous import S
from qa_guru_python_3_14.schemas.user import post_create_user

body_post_create_user = {
          "name": "morpheus",
          "job": "leader"
       }

credentials_for_registration = {
    "email": "eddddfvfvv@reqres.in",
    "password": "lic3423ka"
    }


def test_post_create_user_status_code(reqresin):
    response = reqresin.post("/api/users", json=body_post_create_user)

    assert response.status_code == 201


def test_post_create_user_has_name(reqresin):
    response = reqresin.post("/api/users", json=body_post_create_user)

    assert response.json().get('name')


def test_post_create_user_schema(reqresin):
    response = reqresin.post("/api/users", json=body_post_create_user)

    assert S(post_create_user) == response.json()


def test_registration_and_login(reqresin):
    registration = reqresin.post("/api/register", json=credentials_for_registration)
    login = reqresin.get("/api/login", json=credentials_for_registration)

    assert login.status_code == 200
