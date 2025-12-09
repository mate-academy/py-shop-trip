from decimal import Decimal

from app.customer import Customer
from app.shop import Shop


class Shopping:
    shopping_registry = []

    def __init__(self, customer: Customer,
                 shop: Shop,
                 fuel_price: Decimal) -> None:
        self.customer = customer
        self.shop = shop
        self.fuel_price = fuel_price
        Shopping.shopping_registry.append(self)

    @property
    def total_amount(self) -> Decimal:
        result = round(self.trip_cost, 2)
        result += round(self.products_cost(), 2)
        return Decimal(result)

    @property
    def trip_cost(self) -> Decimal:
        customer_location = self.customer.location
        shop_location = self.shop.location
        distance = ((customer_location[0] - shop_location[0]) ** 2
                    + (customer_location[1] - shop_location[1]) ** 2) ** 0.5
        one_km_consumption = self.trip_fuel_consumption() / 100
        distance_consumption = distance * one_km_consumption
        cost = distance_consumption * self.fuel_price
        hither_and_thither = cost * 2
        result = round(hither_and_thither, 2)
        return Decimal(result)

    def trip_fuel_consumption(self) -> float:
        customer_car = self.customer.car
        result = customer_car.get("fuel_consumption")
        return result

    def products_cost(self) -> Decimal:
        result = 0.00
        customer_products = self.customer.product_cart
        for one_product, quantity in customer_products.items():
            one_product_price = self.shop.products.get(one_product)
            result += one_product_price * quantity
        result = round(result, 2)
        result_str = str(result)
        result = Decimal(result_str)
        return Decimal(result)
