# Лушников Станислав, 7-й поток — Финальный проект. Инженер по тестированию плюс
import data as d
import sender_stand_request as ssr


# Создать заказ
def create_order(body):
    # получить ответ после создания заказа
    response = ssr.request_create_order(d.headers, body)

    # получить track
    assert response.status_code == 201
    return response.json()['track']


# Получить заказ
def get_order(track):
    # подготовка данных
    order_param = d.param.copy()
    order_param['t'] = track

    # Запрос на получение заказа
    response = ssr.request_get_order(order_param)
    assert response.status_code == 200, f'Получен статус код: {response.status_code}'


# Создание набора тест
def test_create_order():
    # 1 Получить тело запроса на создание заказа
    body = d.order_dict.copy()

    # 2 Создать заказ и получить трек
    track = create_order(body)

    # 3 Получить информацию о заказе
    get_order(track)
