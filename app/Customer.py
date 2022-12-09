class Customer:
    def __init__(
        self,
        person_name: str,
        person_cart: dict,
        person_location: list,
        person_money: int,
        person_car: dict,
        fuel_price: int,
    ) -> None:
        self.fuel_price = fuel_price
        self.person_name = person_name
        self.person_cart = person_cart
        self.person_location = person_location
        self.person_money = person_money
        self.person_car = person_car

    def get_info(self) -> str:
        return f"{self.person_name} has {self.person_money} dollars"

    def get_count(self, product: str) -> str:
        return self.person_cart[product]
