from math import sqrt
import datetime

from ..car.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.products = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def choose_shop(self, shops: list, fuel_price: float) -> tuple:
        shop_expences = []
        for index, shop in enumerate(shops):
            x1, y1, x2, y2 = *self.location, *shop.location
            distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
            fuel_expences = fuel_price * distance
            product_expences = sum(shop.products[item] * count
                                   for item, count in self.products.items())
            total = round(product_expences + fuel_expences * 2, 2)

            print(f"{self.name}'s trip to the {shop.name} costs {total}")

            shop_expences.append((shop, total, product_expences))
        return min(shop_expences, key=lambda x: x[1])

    def visit_shop(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        shop, total, product_expences = self.choose_shop(shops, fuel_price)

        if total <= self.money:
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"{self.name} rides to {shop.name}\n\n"
                  f"Date: {date}\n"
                  f"Thanks, {self.name}, for your purchase!\n"
                  "You have bought: ")

            for product, quantity in self.products.items():
                total_price = shop.products[product] * quantity
                if total_price % 1 == 0:
                    print(f"{quantity} {product}s for "
                          f"{int(total_price)} dollars")
                else:
                    print(f"{quantity} {product}s for "
                          f"{total_price} dollars")

            print(f"Total cost is {product_expences} dollars\n"
                  "See you again!\n\n"
                  f"{self.name} rides home\n"
                  f"{self.name} now has {self.money - total} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  "to make a purchase in any shop")
