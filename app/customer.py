class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def sum_products(self, product_shop: dict) -> float:
        return sum([quantity * product_shop[name_product]
                    for name_product, quantity in self.product_cart.items()
                    if name_product in product_shop])

    def cost_trip(self, distance: float, fuel_price: float) -> float:
        return (self.car["fuel_consumption"] / 100
                ) * (distance * 2) * fuel_price
