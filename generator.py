import requests
import random
import string
import json
from static_data import TestAPICourierLinks, TestAPIOrdersLinks, TestOrder


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return response, login_pass


def non_existing_courier_id():
    courier = register_new_courier_and_return_login_password()
    sign_in = {
        "login": courier[1][0],
        "password": courier[1][1]
    }

    courier_signin = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=sign_in)
    courier_id = courier_signin.json()["id"] + random.randint(1000, 9999)
    return courier_id


def create_new_order():
    payload = json.dumps(TestOrder.test_order)
    response = requests.post(TestAPIOrdersLinks.main_url + TestAPIOrdersLinks.main_orders_url, data=payload)
    track = response.json()["track"]
    return track


