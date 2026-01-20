from app.mixins.cash_register_mixin import CashRegisterMixin


class Shop(CashRegisterMixin):
    def __init__(
            self,
            name: str,
            location: list[int],
            product_prices: dict
    ) -> None:
        self.name = name
        self.location = location
        self.product_prices = product_prices
