from math import sqrt
from app.customer import Customer
from app.car import Car


class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict,
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def product_cost(self, customer: Customer) -> float:
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        return milk_cost + bread_cost + butter_cost

    def cost_trip(self,
                  car: Car,
                  customer: Customer,
                  fuel_price: float | int,
                  ) -> float:
        location = sqrt((self.location[0] - customer.location[0]) ** 2
                        + (self.location[1] - customer.location[1]) ** 2)
        cost_fuel = location * fuel_price * car.fuel_consumption / 100
        return round(cost_fuel * 2, 2)
