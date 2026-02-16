class Customer:
    def __init__(
            self,
            person_name: str,
            product_cart: dict,
            person_location: list,
            money: float,
            car: dict
    ) -> None:
        self.person_name = person_name
        self.product_cart = product_cart
        self.person_location = person_location
        self.money = money
        self.car = car
