from app.car import Car
from app.customer import Customer
from app.location import Location
from app.shop import Shop


class Parser:
    def __init__(self, data: dict) -> None:
        self._data = data

    def parse_data(self) -> tuple[float | int, list[Customer], list[Shop]]:
        fuel_price = self._data.get("FUEL_PRICE", 0)

        customers = []
        for customer_data in self._data.get("customers", []):
            car_data = customer_data["car"]
            new_customer = Customer(
                _name=customer_data["name"],
                _product_cart=customer_data["product_cart"],
                _location=Location(*customer_data["location"]),
                _money=customer_data["money"],
                _car=Car(car_data["brand"], car_data["fuel_consumption"])
            )
            customers.append(new_customer)

        shops = []
        for shop_data in self._data.get("shops", []):
            new_shop = Shop(
                _name=shop_data["name"],
                _location=Location(*shop_data["location"]),
                _products=shop_data["products"]
            )
            shops.append(new_shop)

        return fuel_price, customers, shops
