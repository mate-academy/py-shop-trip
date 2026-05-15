from decimal import Decimal

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: tuple,
            money: Decimal,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home = location
        self.money = money
        self.car = car

    def measure_distance(self, dest: tuple) -> Decimal:
        return Decimal(
            (
                (dest[0] - self.location[0]) ** 2
                + (dest[1] - self.location[1]) ** 2
            ) ** 0.5
        )

    def calculate_fuel_cost(self, dest: tuple, fuel_price: Decimal) -> Decimal:
        return Decimal(
            fuel_price
            * self.measure_distance(dest)
            * self.car.fuel_consumption / Decimal(100)
        )

    def travel(self, dest: tuple, fuel_price: Decimal) -> Decimal:
        travel_cost = self.calculate_fuel_cost(dest, fuel_price)
        self.location = dest
        return travel_cost

    def shopping(self, shops: dict, fuel_price: Decimal) -> None:
        print(f"{self.name} has {round(self.money, 2).normalize()} dollars")

        shop_costs = {}

        for shop in shops.values():
            estimated_cost = (
                (2 * self.calculate_fuel_cost(shop.location, fuel_price))
                + shop.calculate_shopping(self.product_cart)
            )
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(estimated_cost, 2).normalize()}"
            )
            shop_costs[shop.name] = estimated_cost

        lowest_cost = min(shop_costs.values())

        if lowest_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return

        lowest_cost_shop = min(shop_costs, key=shop_costs.get)

        target_shop = shops[lowest_cost_shop]

        print(f"{self.name} rides to {target_shop.name}\n")
        self.money -= self.travel(target_shop.location, fuel_price)

        self.money -= target_shop.shopping(self)

        print(f"\n{self.name} rides home")
        self.money -= self.travel(self.home, fuel_price)

        print(
            f"{self.name} now has "
            f"{round(self.money, 2).normalize()} dollars\n"
        )
