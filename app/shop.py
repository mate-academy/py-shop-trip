from __future__ import annotations
from math import sqrt


from app.customer import Customer


class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, customer: Customer) -> float:
        x1, y1 = customer.location
        x2, y2 = self.location
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def calculate_fuel_cost(self,
                            customer: Customer,
                            fuel_price: float) -> float:
        distance = self.calculate_distance(customer)
        fuel_spent = distance * customer.car.fuel_consumption / 100
        return fuel_spent * fuel_price

    def calculate_shopping_cost(self,
                                customer: Customer,
                                fuel_price: float) -> float:
        fuel_cost = self.calculate_fuel_cost(customer, fuel_price) * 2
        total_bill = self.calculate_total_bill(customer.product_cart)
        return round(fuel_cost + total_bill, 2)

    def calculate_product_price(self,
                                product_name: str,
                                product_cart: dict) -> float:
        return product_cart[product_name] * self.products[product_name]

    def calculate_total_bill(self, product_cart: dict) -> float:
        total_cost = 0
        for product in product_cart.keys():
            if product in self.products:
                total_cost += self.calculate_product_price(product,
                                                           product_cart)
        return total_cost

    def customer_receipt(self, customer: Customer) -> None:
        cart = customer.product_cart
        print(f"\nDate: 04/01/2021 12:33:41\nThanks, {customer.name}, "
              f"for your purchase!\nYou have bought: ")
        for product, quantity in cart.items():
            print(f"{quantity} {product}s for "
                  f"{self.calculate_product_price(product, cart)} dollars")
        print(f"Total cost is {self.calculate_total_bill(cart)} dollars"
              f"\nSee you again!")

    def best_shop_visit(self,
                        customer: Customer,
                        min_trip_cost: float) -> None:
        print(f"{customer.name} rides to {self.name}")
        self.customer_receipt(customer)
        customer.money -= min_trip_cost
        print(f"\n{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")

    def choosing_shop(self,
                      customer: Customer,
                      fuel_price: float,
                      min_trip_cost: float,
                      best_shop: Shop) -> list:
        trip_cost = self.calculate_shopping_cost(customer, fuel_price)
        print(f"{customer.name}'s trip to "
              f"the {self.name} costs {trip_cost}")
        if trip_cost < min_trip_cost and trip_cost <= customer.money:
            min_trip_cost = trip_cost
            best_shop = self
        return [min_trip_cost, best_shop]
