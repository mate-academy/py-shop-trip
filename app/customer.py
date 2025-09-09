from decimal import Decimal
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = [Decimal(str(loc)) for loc in location]
        self.money = Decimal(str(money))

        self.car = car
        self.car['fuel_consumption'] = Decimal(str(self.car['fuel_consumption']))

    def check_price_products(self, shop: Shop) -> Decimal:
        return sum([shop.products[product] * self.product_cart[product]
                    for product in self.product_cart.keys()])

    def from_to_shop(self, fuel_price: Decimal, shop: Shop) -> Decimal:
        way_to_shop = (
            (shop.location[0] - self.location[0]) ** 2 + (shop.location[1] - self.location[1]) ** 2).sqrt()

        fuel_needed = (way_to_shop / Decimal('100')) * self.car["fuel_consumption"]
        trip_price = fuel_needed * fuel_price
        return trip_price
