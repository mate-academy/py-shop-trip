from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products_cart: dict,
            location: list[int],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.products_cart = products_cart
        self.location = location
        self.money = money
        self.car = car

    def trip_price(self, fuel_price: int | float, shop: Shop) -> int | float:
        distance = (
            (
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2
            ) ** 0.5
        )
        fuel_cost = (
            fuel_price
            * (self.car["fuel_consumption"] / 100)
            * distance * 2
        )
        products_price = sum(
            [shop.products[product] * amount
             for product, amount in self.products_cart.items()]
        )

        return fuel_cost + products_price
