from qa_guru_python_3_14.schemas.user import single_user_schema
from pytest_voluptuous import S


def test_get_single_user_status_code(reqresin):
    response = reqresin.get("/api/users/1")

    assert response.status_code == 200


def test_get_single_user_has_first_name(reqresin):
    response = reqresin.get("/api/users/1")

    assert response.json().get('data').get('first_name')


def test_get_single_user_email_has_reqres_ru(reqresin):
    response = reqresin.get("/api/users/1")

    email = response.json().get('data').get('email')

    assert "@reqres.in" in email


def test_get_single_user_schema(reqresin):
    response = reqresin.get("/api/users/1")

    assert S(single_user_schema) == response.json()
