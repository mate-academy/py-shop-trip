from typing import Dict


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: "Location",
            money: int,
            car: "Car"
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = location
        self.current_location = self.home_location
        self.money = money
        self.car = car

    def calc_price_to_shop(self, shop: "Shop", fuel_price: float) -> tuple:
        distance = self.current_location.calculate_distance(shop.location)
        consumption = self.car.fuel_consumption / 100 * distance
        fuel_consumption_price = consumption * fuel_price * 2
        products_cost = 0

        for product, amount in self.product_cart.items():
            products_cost += shop.get_price_on_products(product, amount)

        result = round(fuel_consumption_price + products_cost, 2)

        print(f"{self.name}'s trip to the {shop.name} costs {result}")

        return self.money > result, {"name": shop, "cost": result}

    def ride_to_shop(self, shop: "Shop", cost: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.current_location = shop.location
        shop.serve_customer(self, cost)

    def ride_to_home(self) -> None:
        self.current_location = self.home_location
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")
