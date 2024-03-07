import datetime

from app.config_loader import load_config
from app.car import Car
from app.shop import Shop

config = load_config()
customers = config["customers"]


class Customer:
    def __init__(self, customer_params: dict) -> None:
        self.name: str = customer_params["name"]
        self.product_cart: dict = customer_params["product_cart"]
        self.location: list[int] = customer_params["location"]
        self.money: int | float = customer_params["money"]
        self.car: Car = Car(customer_params["car"])

    def trip_cost(self, shop: Shop) -> int | float:
        customer_x, customer_y = self.location
        shop_x, shop_y = shop.location
        point_x = shop_x - customer_x
        point_y = shop_y - customer_y
        distance_to_shop = (point_x ** 2 + point_y ** 2) ** 0.5
        cost_per_km = self.car.fuel_consumption / 100 * self.car.FUEL_PRICE
        cost_dist_shop_and_back = round(distance_to_shop * cost_per_km * 2, 2)

        cost_buy_all_products = 0
        for product in shop.products:
            product_amount = self.product_cart[product.name]
            cost_buy_all_products += product_amount * product.price

        return cost_dist_shop_and_back + cost_buy_all_products

    def choose_nearest_shop(self, shops: list[Shop]) -> Shop:
        nearest_shop = shops[0]
        for shop in shops:
            if self.trip_cost(shop) < self.trip_cost(nearest_shop):
                nearest_shop = shop
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {self.trip_cost(shop)}")
        return nearest_shop

    def buy_products_in_shop(self, shop: Shop) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total = 0
        for product in shop.products:
            product_amount = self.product_cart[product.name]
            product_cost = product.price * product_amount
            if product_cost.is_integer():
                product_cost = int(product_cost)

            total += product_cost
            print(f"{product_amount} {product.name}s"
                  f" for {product_cost} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
