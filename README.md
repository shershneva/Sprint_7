Тесты для API ручек сайта YaScooter.
Используются библиотеки random, datetime, string для тестовых данных. 
Для запросов используются библиотеки json и requests.
Для генерации отчетов используется библиотека allure, для запуска тестов pytest.

### Файл generator содержит фукции: ###
register_new_courier_and_return_login_password - генерация нового курьера
non_existing_courier_id - генерация несуществующего id курьера
create_new_order - генерация нового заказа

### Файл static_data: ###
содержит тестовые ссылки и другие статические данные

## TestCourierCreateAPI: ##
Тесты ручки создания курьера:
- test_courier_create_new_courier_success — успешное создание курьера
- test_courier_create_already_existing_user_fail — создание курьера с существующими данными
- test_courier_create_no_data_fail — создание курьера с неполным набором данных

## TestCourierLoginAPI: ##
Тесты ручки логина курьера:
- test_courier_login_success — успешный логин курьера
- test_courier_login_no_such_user_fail — логин с несуществующими данными
- test_courier_login_no_data_fail — логин с недостаточными данными (падает на отправке только логина)

## TestCourierDeleteAPI: ##
- test_courier_delete_success — успешное удаление курьера
- test_courier_delete_no_id_fail — удаление при несуществующем id
- test_courier_delete_without_id_fail - удаление при отправке без id в теле (падает, так как без id в теле запроса курьер все равно удаляется)

## TestGetOrdersList: ##
- test_get_orders_list_success - успешное получение списка заказов

## TestCreateOrder: ##
- test_order_creation_with_different_colors_success - успешное создание заказа с разными цветами

## TestTrackOrder: ##
- test_order_track_success - успешное получение заказа
- test_order_track_no_order_id_fail - получение заказа без номера
- test_order_track_wrong_order_id_fail - получение заказа с некорректным номером

## TestAcceptOrder: ##
- test_order_accept_success - успешный акцепт заказа
- test_order_accept_no_сourier_id_fail - акцепт без id клиента
- test_order_accept_no_order_id_fail - акцепт без номера заказа (падает)
- test_order_accept_wrong_courier_id_fail - акцепт с некорректным курьером


