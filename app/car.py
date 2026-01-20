from math import sqrt
from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def car_expenses(
            self,
            fuel_price: float,
            customer: Customer,
            shop: Shop
    ) -> float:
        distance = 0

        for i in range(len(customer.location)):
            distance += (shop.location[i] - customer.location[i]) ** 2

        consumption = (
            round(
                fuel_price * self.fuel_consumption * sqrt(distance) * 2 / 100,
                2
            )
        )
        return consumption

    def total_expenses(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> float:
        return (
            shop.shop_expenses(customer)
            + self.car_expenses(fuel_price, customer, shop)
        )

    def trip_info(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> None:
        print(f"{customer.name}'s trip to the {shop.name} costs"
              f" {self.total_expenses(customer, shop, fuel_price)}")

    def come_back_info(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> None:
        total_expenses = self.total_expenses(customer, shop, fuel_price)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - total_expenses} dollars\n")
