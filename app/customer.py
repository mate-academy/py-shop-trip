import datetime
from typing import Optional

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def define_shop(self, shops: list[Shop],
                    fuel_price: float) -> Optional[Shop]:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip_cost = 0
        selected_shop: Optional[Shop] = None

        for shop in shops:
            fuel_cost = self.car.calculate_fuel_cost(self.location,
                                                     shop.location, fuel_price)
            products_cost = sum(
                product_value * shop.products.get(product, 0)
                for product, product_value in self.products.items()
            )
            trip_cost = round(fuel_cost * 2 + products_cost, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

            if not cheapest_trip_cost or trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                selected_shop = shop

        if cheapest_trip_cost > self.money:
            print(f"{self.name} doesn't have enough money to "
                  f"make a purchase in any shop")
            return None

        self.money -= cheapest_trip_cost
        print(f"{self.name} rides to {selected_shop.name}\n")
        return selected_shop

    def make_purchase(self, selected_shop: Shop) -> None:
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in self.products.items():
            product_price = selected_shop.products.get(product, 0)
            cost = product_price * quantity
            if isinstance(cost, (int, float)) and float(cost).is_integer():
                cost = int(cost)
            total_cost += cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
