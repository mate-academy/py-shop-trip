from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            money: int,
            product_cart: dict,
            car: dict
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.money = money
        self.product_cart = product_cart
        self.car = Car(**car)

    def find_distance(self, shop_location: list) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location

        return ((x2 - x1)**2 + (y2 - y1) ** 2) ** 0.5

    def make_purchase(self, shop: Shop) -> None:
        cost = 0
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {self.name}, for your purchase!\nYou have bought:")
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                price = shop.products[product] * quantity
                price = int(price) if price == int(price) else price
                cost += price
                print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {cost} dollars\nSee you again!")
