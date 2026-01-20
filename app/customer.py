from math import sqrt


from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def cash_flow(self,
                  list_of_shops: list[Shop],
                  fuel_price: float) -> dict:
        dict_of_costs = {"shop": "default", "cost": 0}

        for shop in list_of_shops:
            cost = (shop.location[0] - self.location[0])**2
            cost += (shop.location[1] - self.location[1])**2
            cost = sqrt(cost)
            cost *= (self.car.fuel_consumption / 100) * fuel_price * 2
            cost = round(cost, 2)
            cost += sum(
                [shop.products[product] * self.product_cart[
                    product
                ] for product in self.product_cart.keys()])

            if dict_of_costs["cost"] == 0 or dict_of_costs["cost"] > cost:
                dict_of_costs.update({"shop": shop, "cost": cost})

            print(f"{self.name}'s trip to the {shop.name} costs {cost}")
        return dict_of_costs
