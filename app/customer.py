from app.shop import Shop
import datetime


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def balance_customer(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculation_trip_shop(self, fuel: float, shop: Shop) -> float:
        trip_cost = (fuel * shop.distance_calculation(self.location)
                          * self.car["fuel_consumption"] / 100)
        for products, number in self.product_cart.items():
            trip_cost += number * shop.products[products]
        return round(trip_cost, 2)

    def trip_to_shop(self) -> None:
        today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {today}\n"
              f"Thanks, {self.name}, for you purchase!\n"
              f"You have bought: ")

    def products_basket(self, shop: Shop) -> None:
        total_cost = 0
        for product, amount in self.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{amount * shop.products[product]} dollars")
            total_cost += (amount * shop.products[product])
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")

    def go_to_home(self, trip_cost: float) -> None:
        money_left = self.money - trip_cost
        print(f"{self.name} rides home\n"
              f"{self.name} now has {money_left} dollars\n")
