from __future__ import annotations

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, *args, **kwargs) -> None:
        customer = None
        if args and isinstance(args[0], dict):
            customer = args[0]
        elif isinstance(kwargs, dict):
            customer = kwargs

        if customer is not None:
            self.name = customer["name"]
            self.money = customer["money"]
            self.location = customer["location"]

            self.product_cart = {}
            self.car = None
        else:
            raise TypeError

    def setproduct(self, products: list) -> None:
        self.product_cart = products

    def setcar(self, car: Car) -> None:
        self.car = car

    @staticmethod
    def get_list_customers(customers_info: dict) -> list(Customer):
        customers = []
        for customer_info in customers_info:
            customer = Customer(customer_info)

            customer.setproduct(customer_info["product_cart"])
            customer.setcar(Car(customer_info["car"]))

            customers.append(customer)
        return customers

    def choose_cheapest_shop(self, shops: list[Shop],
                             fuel_price: float) -> Shop:
        result = 0
        result_shop = None

        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            result_temp = self.calculate_costs_shop(shop, fuel_price)
            if result_temp is not None:
                print(f"{self.name}'s trip to the {shop.name}"
                      f" costs {result_temp}")
                if result == 0 or result_temp < result:
                    result = result_temp
                    result_shop = shop
            else:
                print(f"{self.name}'s trip to the {shop.name} impossible")

        if result <= self.money and result_shop:
            print(f"{self.name} rides to {result_shop.name}\n")
            result_shop.visit_store(self)
            self.money = round(self.money - result, 2)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money} dollars\n")

            return result_shop

        print(f"{self.name} doesn't have enough money"
              f" to make purchase in any shop")
        return None

    def calculate_costs_shop(self, shop: object, fuel_price: float) -> float:
        cost = 0
        for demand, demand_quantity in self.product_cart.items():
            if demand in shop.products:
                cost += demand_quantity * shop.products[demand]
            else:
                return None

        distance = (abs(shop.location[0] - self.location[0]) ** 2
                    + abs(shop.location[1] - self.location[1]) ** 2) ** 0.5
        fuel = self.car.calculate_fuel(distance)
        fuel_cost = fuel * fuel_price

        return round(cost + fuel_cost * 2, 2)
