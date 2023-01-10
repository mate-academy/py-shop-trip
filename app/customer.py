from app.car import Car


class Customer:

    def __init__(
            self,
            customer_dict: dict
    ) -> None:
        self.name = None
        self.product_cart = None
        self.location = None
        self.money = None
        self.car = None
        for key, value in customer_dict.items():
            setattr(self, key, value)
        self.car = Car(
            brand=self.car["brand"],
            consumption=self.car["fuel_consumption"]
        )
