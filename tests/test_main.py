# tests/test_main.py

import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Добавляем путь к app в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.main import shop_trip

# Фикстура для конфигурации
@pytest.fixture
def config():
    return {
        "FUEL_PRICE": 2.4,
        "customers": [
            {
                "name": "Bob",
                "product_cart": {
                    "milk": 4,
                    "bread": 2,
                    "butter": 5
                },
                "location": [12, -2],
                "money": 55,
                "car": {
                    "brand": "Suzuki",
                    "fuel_consumption": 9.9
                }
            },
            {
                "name": "Monica",
                "product_cart": {
                    "milk": 3,
                    "bread": 3,
                    "butter": 1
                },
                "location": [11, -2],
                "money": 12,
                "car": {
                    "brand": "Audi",
                    "fuel_consumption": 7.6
                }
            }
        ],
        "shops": [
            {
                "name": "Outskirts Shop",
                "location": [10, -5],
                "products": {
                    "milk": 3,
                    "bread": 1,
                    "butter": 2.5
                }
            },
            {
                "name": "Shop '24/7'",
                "location": [4, 3],
                "products": {
                    "milk": 2,
                    "bread": 1.5,
                    "butter": 3.2
                }
            }
        ]
    }

# Тест функции shop_trip
def test_shop_trip(config, capsys):
    # Мокаем open и json.load
    with patch("builtins.open", MagicMock()) as mock_open, \
         patch("json.load", return_value=config):

        # Мокаем datetime в модуле shop
        with patch("app.shop.datetime") as mock_datetime:
            # Устанавливаем возвращаемое значение для now()
            mock_now = MagicMock()
            mock_now.strftime.return_value = "04/01/2021 12:33:41"
            mock_datetime.now.return_value = mock_now

            # Вызываем функцию shop_trip
            shop_trip()

            # Получаем вывод
            captured = capsys.readouterr()
            output = captured.out

            # Проверяем вывод для Bob
            assert "Bob has 55 dollars" in output
            assert "Bob's trip to the Outskirts Shop costs 28.21" in output
            assert "Bob's trip to the Shop '24/7' costs 31.48" in output
            assert "Bob rides to Outskirts Shop" in output
            assert "Date: 04/01/2021 12:33:41" in output  # Проверка даты и времени
            assert "Thanks, Bob, for your purchase!" in output
            assert "4 milks for 12 dollars" in output
            assert "2 breads for 2 dollars" in output
            assert "5 butters for 12.5 dollars" in output
            assert "Total cost is 26.5 dollars" in output
            assert "See you again!" in output
            assert "Bob rides home" in output
            assert "Bob now has 26.79 dollars" in output

            # Проверяем вывод для Monica
            assert "Monica has 12 dollars" in output
            assert "Monica's trip to the Outskirts Shop costs 15.65" in output
            assert "Monica's trip to the Shop '24/7' costs 16.84" in output
            assert "Monica doesn't have enough money to make a purchase in any shop" in output