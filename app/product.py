from decimal import Decimal


class Product:

    def __init__(
            self,
            name: str,
            price: Decimal
    ) -> None:
        self.name = name
        self.price = price
