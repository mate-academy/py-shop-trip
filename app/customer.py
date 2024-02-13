# customer.py
import datetime
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = (
            (self.location[0] - shop.location[0])**2
            + (self.location[1] - shop.location[1])**2
        )**0.5
        fuel_needed = self.car.fuel_consumption * distance_to_shop / 100
        fuel_cost = fuel_needed * fuel_price
        product_cost = sum(
            self.product_cart[product] * shop.products.get(product, 0)
            for product in self.product_cart
        )
        total_cost = 2 * fuel_cost + product_cost  # round trip
        return total_cost

    def go_shopping(self, shops: list[Shop], fuel_price: float) -> None:
        money = f"{self.money:.2f}"
        print(f"{self.name} has {money} dollars")
        costs = [
            (shop.name, self.calculate_trip_cost(shop, fuel_price))
            for shop in shops
        ]
        for shop_name, cost in costs:
            print(f"{self.name}'s trip to the {shop_name} costs {cost:.2f}")
        cheapest_shop_name, cheapest_cost = min(costs, key=lambda x: x[1])
        cheapest_shop = next(
            shop for shop in shops if shop.name == cheapest_shop_name
        )
        if cheapest_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
        else:
            self.money -= cheapest_cost
            print(f"{self.name} rides to {cheapest_shop_name}")
            print(
                f"Date: "
                f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
            )
            print(f"Thanks, {self.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in self.product_cart.items():
                product_price = (
                    cheapest_shop.products[product] * quantity
                )
                product_price = f"{product_price:.2f}"
                print(f"{quantity} {product}s for {product_price} dollars")
            cheapest_cost = f"{cheapest_cost:.2f}"
            print(f"Total cost is {cheapest_cost} dollars")
            print("See you again!")
            print(f"{self.name} rides home")
            self.money = f"{self.money:.2f}"
            print(f"{self.name} now has {self.money} dollars")
