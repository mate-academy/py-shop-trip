class Car:

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car

    def print_money_remainder(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def ride_home_and_show_remainder(self) -> None:
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {round(self.money, 2)} dollars\n"
        )


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products_provides: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_provides = products_provides
