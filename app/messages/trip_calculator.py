from math import sqrt

from app.customers.customer import Customer
from app.days.day import DayMark
from app.messages.keys import DictKeys
from app.shops.shop import Shop


class Calculator:
    def __init__(self,
                 customer: Customer,
                 shops: list[Shop],
                 day: DayMark) -> None:
        self.keys = DictKeys()
        self.customer = customer
        self.shops = shops
        self.day = day
        self.trips_checks = self.__get_trip_checks()

    def __calculate_distance(self, shop: Shop) -> float:
        cust_x, cust_y = self.customer.location
        shop_x, shop_y = shop.location
        distance = sqrt((shop_x - cust_x) ** 2 + (shop_y - cust_y) ** 2)
        return distance

    def __calculate_trip_price(self, shop: Shop) -> float | int:
        distance = self.__calculate_distance(shop=shop)
        fuel_price = self.day.fuel_price
        fuel_consumption = self.customer.car.fuel_consumption
        trip_cost = (distance / 100) * fuel_consumption * fuel_price
        return trip_cost

    def __get_prices_dict(self, shop: Shop) -> dict:
        customer_products = self.customer.product_cart.items()
        shop_products = shop.products
        all_products_price = 0
        output = {}
        for product, numbers in customer_products:
            if product in shop_products:
                product_price = numbers * shop_products[product]
                round_price = round(product_price, 1)
                clean_price = round_price if (
                        str(round_price)[-1] != "0") else int(round_price)
                all_products_price += clean_price
                output[product] = clean_price

        way_price = self.__calculate_trip_price(shop)
        total_price = all_products_price + (way_price * 2)
        output[self.keys.store_check] = all_products_price
        output[self.keys.trip_price] = round(total_price, 2)
        return output

    def __get_trip_checks(self) -> dict:
        trip_prices = {}
        for shop in self.shops:
            prices = self.__get_prices_dict(shop)
            trip_prices[shop.name] = prices
        return trip_prices

    def __get_minimal_trip_price(self) -> int | float | None:
        trip_prices = []
        for shop_name, check in self.trips_checks.items():
            price = check[self.keys.trip_price]
            trip_prices.append(price)
        minimal_trip_price = min(trip_prices)
        return minimal_trip_price

    def get_shop_check(self) -> dict | None:
        money = self.customer.money
        minimal_trip_price = self.__get_minimal_trip_price()
        for shop_name, check in self.trips_checks.items():
            if (money >= minimal_trip_price
                    and check[self.keys.trip_price] == minimal_trip_price):
                current_check = self.trips_checks[shop_name]
                current_check[self.keys.shop_name] = shop_name
                return current_check
        return None
