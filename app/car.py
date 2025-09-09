from decimal import Decimal
from app.customer import Customer
from app.shop import Shop


class Car(Customer):
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: dict
    ) -> None:

        super().__init__(name, product_cart, location, money)
        self.car = car
        self.car['fuel_consumption'] = Decimal(str(self.car['fuel_consumption']))

    def from_to_shop(self, fuel_price: Decimal, shop: Shop) -> Decimal:
        way_to_shop = (
            (shop.location[0] - self.location[0]) ** 2 + (shop.location[1] - self.location[1]) ** 2
        ).sqrt()

        fuel = (way_to_shop / Decimal('100')) * self.car["fuel_consumption"]
        price_go_to_shop = fuel * fuel_price
        return price_go_to_shop
