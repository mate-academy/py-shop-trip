from decimal import Decimal


class Products:
    def __init__(self, milk: Decimal, bread: Decimal, butter: Decimal) -> None:
        self.milk = milk
        self.bread = bread
        self.butter = butter
