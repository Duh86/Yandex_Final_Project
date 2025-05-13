# Пётр Кутузов, 29-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_PATH

def test_create_and_get_order():
    create_response = requests.post(BASE_URL + CREATE_ORDER_PATH, json={
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    })
    assert create_response.status_code == 201
    track = create_response.json().get("track")
    assert track is not None

    get_response = requests.get(BASE_URL + GET_ORDER_PATH, params={"t":track})
    assert get_response.status_code == 200