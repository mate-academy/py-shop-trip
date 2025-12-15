class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_trip(self, fuel_price: float, distance: float) -> float:
        price = (distance / 100) * self.fuel_consumption * fuel_price
        return round(price * 2, 2)


class Customer:
    def __init__(
        self, name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def return_home(self, receipt: int | float) -> None:
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {receipt} dollars\n"
        )
