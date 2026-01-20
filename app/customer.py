from app.shop import Shop
import math
import datetime
data = datetime.datetime(2021, 1, 4, 12, 33, 41)


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: int, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, to_location: list) -> float:
        return math.sqrt((self.location[0] - to_location[0]) ** 2
                         + (self.location[1] - to_location[1]) ** 2)

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        fuel_needed = (distance / 100) * self.car["fuel_consumption"]
        return fuel_needed * fuel_price

    def total_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_there_and_back = 2 * self.fuel_cost(distance, fuel_price)

        product_total = 0
        for item, quantity in self.product_cart.items():
            if item not in shop.products:
                return float("inf")
            product_total += shop.products[item] * quantity

        return fuel_there_and_back + product_total

    def buy_products(self, shop: Shop) -> None:

        print(f"\nDate: {data.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product_name, quantity in self.product_cart.items():
            price = shop.get_product_price(product_name)
            cost = price * quantity
            total_cost += cost
            print(f"{quantity} {product_name}s for {cost:g} dollars")

        print(f"Total cost is {total_cost:g} dollars")
        print("See you again!")

        self.location = shop.location
