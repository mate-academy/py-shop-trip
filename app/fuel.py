from decimal import Decimal


class Fuel:

    def __init__(self, price: Decimal) -> None:
        self.price = Decimal(price)
