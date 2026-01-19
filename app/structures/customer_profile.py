from app.structures.coords import Coords


class Car:
    fuel_price = None

    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __getitem__(self) -> str | float:
        return self

    @classmethod
    def set_fuel_price(cls, fuel_price: float) -> None:
        cls.fuel_price = fuel_price


class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            product_cart: dict,
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.location = Coords(*location)
        self.product_cart = product_cart
        self.money = money
        self.car = car
        self.home = Coords(*location)

    def wallet(self) -> None:
        print(f"{self.name} has {self.money} dollars")
