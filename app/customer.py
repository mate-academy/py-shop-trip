from decimal import Decimal, ROUND_HALF_UP

from app.car import Car
from app.location import Location


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int, int],
        money: Decimal,
        car_data: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = Location(*location)
        self.money = Decimal(str(money))
        self.car = Car(**car_data)
        self.home_location = self.location

    def find_cheapest(
            self,
            shops: list,
            fuel_price: Decimal
    ) -> tuple:
        all_shops_total = {}
        for shop in shops:
            fuel_cost = self.car.count_fuel_cost(
                self.location,
                shop.location,
                fuel_price
            )
            products_cost = self.count_prod_cost(shop.products)
            total = ((fuel_cost + products_cost).
                     quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

            all_shops_total[shop] = total

            print(f"{self.name}'s trip to the {shop.name} costs {total}")

        cheapest_shop = min(all_shops_total, key=all_shops_total.get)
        return cheapest_shop, all_shops_total[cheapest_shop]

    def count_prod_cost(self, prices: dict) -> Decimal:
        sum_prod_cost = Decimal("0")

        for count, price in zip(self.product_cart.values(), prices.values()):
            sum_prod_cost += count * Decimal(str(price))

        return sum_prod_cost

    def ride_to(self, destination: Location, place_name: str) -> None:
        self.location = destination
        print(f"{self.name} rides to {place_name}\n")

    def pay_and_back(self, spending: Decimal) -> None:
        self.money -= spending
        self.location = self.home_location
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")
