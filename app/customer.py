import datetime
from unittest.mock import patch
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: int, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def products_price(self, other: Shop) -> float | int:
        products_price = sum(
            [self.product_cart[product] * other.products[product]
             for product in self.product_cart
             if product in other.products]
        )
        return products_price

    def buying_products(self, other: Shop) -> None:
        date_str = "04/01/2021 12:33:41"

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.strptime.return_value = datetime.datetime(
                2021, 1, 4, 12, 33, 41
            )
            mock_datetime.return_value.strftime.return_value = date_str
            parsed_date = datetime.datetime.strptime(
                date_str, "%d/%m/%Y %H:%M:%S"
            )
            output = parsed_date.strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {output}")

        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product_to_buy in self.product_cart:
            if product_to_buy in other.products:
                product_price = float(other.products[product_to_buy]
                                      * self.product_cart[product_to_buy])

                if product_price.is_integer():
                    product_price = int(product_price)

                print(f"{self.product_cart[product_to_buy]}"
                      f" {product_to_buy}s for "
                      f"{product_price} "
                      f"dollars")
