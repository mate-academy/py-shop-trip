import math

from app.shop import Shop


class Customer:
    fuel_price = 0

    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def begin_shopping(self, shops: list[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        best_shop, price = self.choose_best_shop(shops)
        if price > self.money:
            print(
                f"{self.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            return
        print(f"{self.name} rides to {best_shop.name}")
        print("")
        best_shop.serve_customer(self, price)

    def choose_best_shop(self, shops: list[Shop]) -> list[Shop, int]:
        cheapest_shop = shops[0]
        cheapest_price = math.inf
        for shop in shops:
            total = round(
                (
                    2 * self.count_distance_price(shop)
                    + self.count_shopping_price(shop)
                ),
                2,
            )
            print(f"{self.name}'s trip to the {shop.name} costs " f"{total}")
            if total < cheapest_price:
                cheapest_shop = shop
                cheapest_price = total
        return [cheapest_shop, cheapest_price]

    def count_distance_price(self, shop: Shop) -> int:
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = shop.location[0]
        y2 = shop.location[1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        price = (
            distance * Customer.fuel_price * self.car["fuel_consumption"] / 100
        )
        return price

    def count_shopping_price(self, shop: Shop) -> int:
        total = 0
        for product_name in self.product_cart.keys():
            quantity = self.product_cart[product_name]
            price = shop.products[product_name]
            total += quantity * price
        return total
