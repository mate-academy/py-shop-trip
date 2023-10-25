from typing import Type


class Client:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_shopping_costs(
            self,
            shops: Type,
            fuel_price: float
    ) -> None:
        self.shopping_costs = {}
        for shop_name, shop in shops.items():
            total_cost = 0
            for product, quantity in self.product_cart.items():
                if product in shop.products:
                    total_cost += shop.products[product] * quantity
            total_cost += self.calculate_trip_cost(shop, fuel_price)

            print(f"{self.name}'s trip to the {shop_name} costs {total_cost}")
            self.shopping_costs[shop_name] = total_cost

    def calculate_trip_cost(
            self,
            shop: Type,
            fuel_price: float
    ) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location

        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        fuel_consumption = self.car["fuel_consumption"]
        cost_of_trip = round(
            (distance / 100) * fuel_consumption * fuel_price * 2, 2
        )

        return cost_of_trip
