from app.customer import Customer
from math import sqrt
from datetime import datetime

class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def check(self, customer: Customer) -> float:
        print("Date: ", datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        full_price = 0
        for product, price in self.products.items():
            if product in customer.product_cart:
                full_price += customer.product_cart[product] * price
                print(f"{customer.product_cart[product]} {product}s for {customer.product_cart[product] * price} dollars")
        print("See you again!")
        customer.money -= full_price
        return full_price

    def trip_price_counting(self, customer: Customer, fuel_price: float) -> None:
        distance = sqrt((self.location[0] - customer.location[0]) ** 2 + (self.location[1] - customer.location[1]) ** 2)
        fuel = (distance * customer.car.fuel_consumption) / 100 * fuel_price
        print(f"{customer.name}'s trip to the {self.name} costs {fuel * 2 + self.check(customer)}")

