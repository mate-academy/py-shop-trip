import json
import dataclasses
import math
import datetime
import os


def format_price(value: float) -> str:
    result = f"{value: .2f}"
    if result.endswith("00"):
        return result[:-3]
    elif result.endswith("0"):
        return result[:-1]
    else:
        return result


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def cost_for_distance(self, distance: float, fuel_price: float) -> float:
        return (self.fuel_consumption / 100) * distance * fuel_price


@dataclasses.dataclass
class Shop:
    name: str
    location: tuple
    products: dict


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: tuple
    money: float
    car: Car

    def __post_init__(self) -> None:
        self.home_location = self.location

    def calculate_total_trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        shop_dist = math.dist(self.location, shop.location)
        fuel_cost = self.car.cost_for_distance(shop_dist * 2, fuel_price)

        items_cost = 0
        for product, quantity in self.product_cart.items():
            price = shop.products.get(product)
            if price is not None:
                items_cost += price * quantity
        total_cost = fuel_cost + items_cost
        return total_cost

    def can_afford_trip(self, shop: Shop, fuel_price: float) -> bool:
        total_cost = self.calculate_total_trip_cost(shop, fuel_price)
        return self.money >= total_cost

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        if self.can_afford_trip(shop, fuel_price):
            self.location = shop.location

            now = datetime.datetime.now()
            print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {self.name}, for your purchase!")
            print("You have bought:")

            total_items_cost = 0
            for product, quantity in self.product_cart.items():
                price = shop.products.get(product)
                if price is not None:
                    product_cost = price * quantity
                    print(f"{quantity} {product}s for"
                          f"{format_price(product_cost)} dollars")
                    total_items_cost += product_cost

            print(f"Total cost is{format_price(total_items_cost)} dollars")
            print("See you again!\n")

            self.location = self.home_location
            total_trip_cost = self.calculate_total_trip_cost(shop, fuel_price)
            self.money -= total_trip_cost
            print(f"{self.name} rides home")
            print(f"{self.name} now has{format_price(self.money)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough"
                  f" money to make a purchase in any shop.\n")


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        fuel_price = config["FUEL_PRICE"]
        shops = []
        for shop_data in config["shops"]:
            shop = Shop(
                name=shop_data["name"],
                location=tuple(shop_data["location"]),
                products=shop_data["products"]
            )
            shops.append(shop)

        customers = []
        for cust_data in config["customers"]:
            car_data = cust_data["car"]
            car = Car(
                brand=car_data["brand"],
                fuel_consumption=car_data["fuel_consumption"]
            )
            customer = Customer(
                name=cust_data["name"],
                product_cart=cust_data["product_cart"],
                location=tuple(cust_data["location"]),
                money=cust_data["money"],
                car=car
            )
            customers.append(customer)

    for customer in customers:
        affordable_options = []
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            cost = customer.calculate_total_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {round(cost, 2)}")

            if customer.can_afford_trip(shop, fuel_price):
                affordable_options.append((cost, shop))

        if affordable_options:
            cheapest_shop = min(affordable_options, key=lambda x: x[0])[1]
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.go_shopping(cheapest_shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
