from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money

    def price_shop(self, shop_products: dict) -> float | int:
        price = 0
        for product in shop_products:
            price += self.product_cart[product] * shop_products[product]

        return price

    def price_trip_in_shop(self, car: Car, shop: Shop) -> float:
        price = (
            car.cost_distance(self.location, shop.location)
        )
        price += self.price_shop(shop.cost_products)
        print(f"{self.name}'s trip to the {shop.name} costs {price}")
        return round(price, 2)

    def buy_in_the_shop(self, price: int | float, name_shop: Shop) -> None:
        self.money -= price
        print(f"{self.name} rides to {name_shop.name}")
        name_shop.print_receipt_purchase(self.name, self.product_cart)
        print()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print()
