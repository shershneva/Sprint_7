import pytest
import allure
from static_data import TestCourier, CourierErrors
from generator import *


class TestCourierCreateAPI:
    @allure.description('Проверяем успешное создание курьера')
    @allure.title('Создание курьера с новыми данными')
    def test_courier_create_new_courier_success(self, delete_user):
        user_data = delete_user[0]

        assert user_data.status_code == 201 and user_data.json()['ok'] == True

    @allure.description('Проверяем создание курьера с использованием уже существующих данных')
    @allure.title('Создание курьера с повторными данными')
    def test_courier_create_already_existing_user_fail(self, delete_user):
        exist_login_courier = {
        "login": delete_user[1][0],
        "password": delete_user[1][1],
        "firstName": delete_user[1][2]
    }

        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url, data=exist_login_courier)

        assert r.status_code == 409 and r.json()['message'] == CourierErrors.error_create_already_exist

    @allure.description('Проверяем создание курьера с недостаточным количеством обязательных данных')
    @allure.title('Создание курьера без обязательных данных')
    @pytest.mark.parametrize('user_data', (TestCourier.create_no_login_courier, TestCourier.create_no_password_courier, TestCourier.create_empty_login,
            TestCourier.create_empty_password))
    def test_courier_create_no_data_fail(self, user_data):
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.error_create_no_data


class TestCourierLoginAPI:
    @allure.description('Проверяем попытку входа с отправкой существующих данных')
    @allure.title('Успешный вход по ручке логина')
    def test_courier_login_success(self, delete_user):
        login_courier = {"login": delete_user[1][0],
                        "password": delete_user[1][1]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 200 and r.json()['id'] > 0

    @allure.description('Проверяем попытку входа с отправкой несуществующих данных')
    @allure.title('Вход с несуществующим юзером')
    def test_courier_login_no_such_user_fail(self, delete_user):
        login_courier = {"login": delete_user[1][1],
                        "password": delete_user[1][0]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)

        assert r.status_code == 404 and r.json()['message'] == CourierErrors.error_login_no_such_user

    @allure.description('Проверяем попытку входа с отправкой недостаточных данных')
    @allure.title('Вход с недостаточными данными')
    @pytest.mark.parametrize('user_data', (TestCourier.login_empty_login, TestCourier.login_empty_password, TestCourier.login_only_password, TestCourier.login_only_login))
    def test_courier_login_no_data_fail(self, user_data):
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.error_login_no_data


class TestCourierDeleteAPI:
    @allure.description('Проверяем удаление курьера с существующим id')
    @allure.title('Успешное удаление курьера')
    def test_courier_delete_success(self):
        user_data = register_new_courier_and_return_login_password()
        login_courier = {"login": user_data[1][0],
                         "password": user_data[1][1]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)
        courier_id = r.json()["id"]
        payload = {"id": courier_id}
        d = requests.delete(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url + str(courier_id), data=payload)

        assert d.status_code == 200 and d.json()['ok'] == True

    @allure.description('Проверяем удаление курьера с несуществующим id')
    @allure.title('Удаление курьера с несуществующим id')
    def test_courier_delete_no_id_fail(self):
        courier_id = non_existing_courier_id()
        payload = {"id": courier_id}
        r = requests.delete(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url + str(courier_id), data=payload)

        assert r.status_code == 404 and r.json()['message'] == CourierErrors.error_delete_no_such_id

    @allure.description('Проверяем удаление курьера без отправки id в теле запроса')
    @allure.title('Удаление курьера без отправки id')
    def test_courier_delete_without_id_fail(self, delete_user):
        login_courier = {"login": delete_user[1][0],
                         "password": delete_user[1][1]}
        r = requests.post(TestAPICourierLinks.main_url + TestAPICourierLinks.login_url, data=login_courier)
        courier_id = r.json()["id"]
        payload = {"id": ""}
        d = requests.delete(TestAPICourierLinks.main_url + TestAPICourierLinks.courier_url + str(courier_id), data=payload)

        assert d.status_code == 400 and d.json()['message'] == CourierErrors.error_delete_no_data











