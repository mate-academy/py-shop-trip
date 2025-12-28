from app.shop import Shop
import json


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def check_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def find_fuel_price(self) -> float:
        with open("app\\config.json", "r") as file:
            file_dict = json.load(file)
            fuel_price = file_dict["FUEL_PRICE"]
            return fuel_price

    def check_distance(self, shop_location: list) -> float:
        distance = ((shop_location[0] - self.location[0]) ** 2
                    + (shop_location[1] - self.location[1]) ** 2) ** 0.5
        return distance

    def check_fuel_per_ride(self, distance: float) -> float:
        return (self.car["fuel_consumption"] / 100) * distance

    def check_price_per_ride(self, shop: Shop) -> float:
        distance = self.check_distance(shop.location)
        fuel_per_ride = self.check_fuel_per_ride(distance)
        fuel_price = self.find_fuel_price()
        ride_cost = fuel_price * fuel_per_ride * 2
        return ride_cost

    def check_product_cart_price(self, shop: Shop) -> float:
        product_cart_price = 0
        for product in self.product_cart:
            products_number = self.product_cart.get(product)
            product_price = shop.products.get(product)
            product_cart_price += (products_number * product_price)
        return product_cart_price

    def check_total_price_per_trip(self, shop: Shop) -> float:
        product_cart_price = self.check_product_cart_price(shop)
        ride_cost = self.check_price_per_ride(shop)
        total_ride_price = round(ride_cost + product_cart_price, 2)
        print(f"{self.name}'s trip to the "
              f"{shop.name} costs {total_ride_price}")
        return total_ride_price

    def make_trip(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")

    def ride_home(self, price_per_trip: float) -> None:
        print(f"{self.name} rides home")
        self.money = round(self.money - price_per_trip, 2)
        print(f"{self.name} now has {self.money} dollars\n")

    def no_trip(self) -> None:
        print(f"{self.name} doesn't have enough money "
              f"to make a purchase in any shop")


def create_customers_list() -> list:
    with open("app\\config.json", "r") as file:
        file_dict = json.load(file)
        customers_file_list = file_dict["customers"]
    customers_list = []
    for customer in customers_file_list:
        customers_list.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ))
    return customers_list
