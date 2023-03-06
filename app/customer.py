# from datetime import datetime
from app.shop import Shop


class Customer:
    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.money = info["money"]
        self.car_consumption = info["car"]["fuel_consumption"]
        self.product_cart = info["product_cart"]
        self.trip_totals = {}

    def select_the_shop(
            self, shops: list[Shop], fuel_price: float
    ) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        totals = []

        for shop in shops:
            trip_cost = round(
                shop.calc_prod_price(self.product_cart)
                + 2
                * fuel_price
                * self.car_consumption
                * shop.calc_distance(self.location)
                / 100,
                2,
            )
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            totals.append(trip_cost)
            self.trip_totals[shop.name] = trip_cost

        if self.money < min(totals):
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
            return None
        the_shop = shops[totals.index(min(totals))]
        print(f"{self.name} rides to {the_shop.name}")
        return the_shop

    def go_shopping(self, shop: Shop) -> None:
        print("")
        # print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for you purchase!\n" f"You have bought: ")
        total_cost = 0
        for product, quantity in self.product_cart.items():
            item_total = shop.products[product] * quantity
            print(f"{quantity} {product}s for {item_total} dollars")
            total_cost += item_total
        print(f"Total cost is {total_cost} dollars\n" f"See you again!\n")
        self.money -= self.trip_totals[shop.name]
        self.go_home()

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
