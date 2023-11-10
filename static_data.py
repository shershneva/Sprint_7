import datetime
from datetime import date as d
class CourierErrors:
    error_login_no_data = "Недостаточно данных для входа"
    error_login_no_such_user = "Учетная запись не найдена"

    error_create_no_data = "Недостаточно данных для создания учетной записи"
    error_create_already_exist = "Этот логин уже используется. Попробуйте другой."

    error_delete_no_data = "Недостаточно данных для удаления курьера"
    error_delete_no_such_id = "Курьера с таким id нет."


class CouriersErrors:
    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_no_such_user = "Курьер не найден"

class OrdersErrors:
    error_track_order_no_data = "Недостаточно данных для поиска"
    error_track_order_no_such_order = "Заказ не найден"

    error_accept_order_no_order_number = "Недостаточно данных для поиска"
    error_accept_order_no_such_courier = "Курьера с таким id не существует"
    error_accept_order_no_data = "Недостаточно данных для поиска"

class TestAPICourierLinks:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    login_url = '/api/v1/courier/login'
    courier_url = '/api/v1/courier/'

    courier_orders_url = '/ordersCount'

class TestAPIOrdersLinks:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    main_orders_url = '/api/v1/orders'
    accept_order_url = '/api/v1/orders/accept/'
    finish_order_url = '/api/v1/orders/finish/'
    cancel_order_url = '/api/v1/orders/cancel'
    track_order_url = '/api/v1/orders/track?t='


class TestCourier:
    login_only_login = {"login": "test_login_1789"}
    login_only_password = {"password": "test_password!"}
    login_empty_password = {"login": "test_login_1789", "password": ""}
    login_empty_login = {"login": "", "password": "test_password!"}

    create_no_login_courier = {"password": "test_password!", "firstName": 'Anyname'}
    create_no_password_courier = {"login": "wrong_courier_11789", "firstName": "Anyname"}
    create_empty_login = {"login": "", "password": "test_password!", "firstName": "Anyname"}
    create_empty_password = {"login": "wrong_courier_11789", "password": "", "firstName": "Anyname"}


class TestOrder:
    delivery_date = (d.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    test_order = {
        "firstName": "Имя",
        "lastName": "Фамилия",
        "address": "ул. 8 марта",
        "metroStation": 21,
        "phone": "+79012345678",
        "rentTime": 3,
        "deliveryDate": delivery_date,
        "comment": "тестовый комментарий"
    }
