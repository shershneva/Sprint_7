import requests
import pytest
from generator import *
from static_data import TestAPICourierLinks


@pytest.fixture()
def delete_user():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url + str(courier_id))
