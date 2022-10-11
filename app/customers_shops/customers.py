from app.customers_shops.shops import Shop
from dataclasses import dataclass
import datetime


@dataclass
class Customer:
    FUEL_PRICE: float
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict
    shops_price = {}

    def calc_price(self, shop: Shop) -> (float, int):
        self.shops_price[shop.name] = {
            "price": 0,
            "fuel": self.calc_fuel(shop),
            "purchase": "",
            "location": shop.location
        }
        for product, amount in self.product_cart.items():
            self.shops_price[shop.name]["price"] +=\
                shop.products[product] * amount
            self.shops_price[shop.name]["purchase"] += (
                f"{amount} {product}s "
                f"for {shop.products[product] * amount} "
                f"dollars\n")
        return round(self.shops_price[shop.name]["price"] +
                     self.shops_price[shop.name]["fuel"] * 2, 2)

    def calc_fuel(self, shop: Shop) -> float:
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** 0.5
        return self.FUEL_PRICE * (distance *
                                  (self.car["fuel_consumption"] / 100))

    def purchase(self) -> None:
        best_shop = min(self.shops_price.items(),
                        key=lambda x: x[1]["price"] + x[1]["fuel"] * 2)[0]
        if self.money >= self.shops_price[best_shop]["price"] +\
                self.shops_price[best_shop]["fuel"] * 2:
            self.money -= self.shops_price[best_shop]["price"] +\
                self.shops_price[best_shop]["fuel"]
            self.location = self.shops_price[best_shop]["location"]
            print(f"{self.name} rides to {best_shop}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {self.name}, for you purchase!")
            print("You have bought: ")
            print(self.shops_price[best_shop]["purchase"][:-1])
            print(f"Total cost is "
                  f"{self.shops_price[best_shop]['price']} dollars")
            print("See you again!\n")
            self.ride_home(best_shop)
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")

    def ride_home(self, best_shop: str) -> None:
        print(f"{self.name} rides home")
        self.money -= self.shops_price[best_shop]["fuel"]
        self.money = round(self.money, 2)
        print(f"{self.name} now has {self.money} dollars\n")
