from math import dist

from car.car import Car


class Customer:
    def __init__(self, fields: dict):
        self.name = fields["name"]
        self.product_cart = fields["product_cart"]
        self.location = fields["location"]
        self.money = fields["money"]
        self.car = Car(fields["car"]["brand"],
                       fields["car"]["fuel_consumption"])

    def show_me_costumers_money(self, when: str = ""):
        """when - means at what point it is
        necessary to display the balance of money"""
        carriage = ""
        if when:
            carriage = "\n"
        return f"{self.name}{when} has {self.money} dollars{carriage}", \
               self.money

    def cost_shopping_trip(self, shop, fuel_price: float):
        liters_per_kilometer = self.car.fuel_consumption / 100
        ride_prise = dist(self.location,
                          shop.location) * liters_per_kilometer * fuel_price
        product_price = sum(
            price * shop.products[product] for product, price in
            self.product_cart.items())
        all_price = round(ride_prise * 2 + product_price, 2)
        return (f"{self.name}'s trip to the {shop.name} "
                f"costs {all_price}", all_price, product_price, shop)

    def direction_to_ride(self, shop=None):
        if shop:
            return f"{self.name} rides to {shop.name}\n"
        return f"{self.name} rides home"
