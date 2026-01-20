from typing import Dict, List
from app.car import Car


class Customer:
    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: List[float], money: float, car: Car) -> None:
        """
        Initialize a Customer instance.

        :param name: The name of the customer.
        :param product_cart: A dictionary of products and their quantities.
        :param location: The customer's location
         as a list of coordinates [x, y].
        :param money: The amount of money the customer has.
        :param car: The customer's car.
        """
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: "Shop", fuel_price: float) -> float:
        """Calculate the total cost of the trip to a shop."""
        distance = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        product_cost = self.calculate_product_cost(shop)
        return round(fuel_cost * 2 + product_cost, 2)

    def calculate_distance(self, shop_location: List[float]) -> float:
        """Calculate the Euclidean distance between customer and shop."""
        return ((self.location[0] - shop_location[0])**2
                + (self.location[1] - shop_location[1])**2)**0.5

    def calculate_product_cost(self, shop: "Shop") -> float:
        """Calculate the total cost of products in the cart."""
        total_cost = 0
        for product, quantity in self.product_cart.items():
            total_cost += shop.products.get(product, 0) * quantity
        return total_cost

    def make_purchase(self, shop: "Shop", fuel_price: float) -> None:
        """Make a purchase at the shop if the customer has enough money."""
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        if self.money >= trip_cost:
            print(f"{self.name} rides to {shop.name}")  # Сообщение о поездке
            self.money -= trip_cost
            self.location = shop.location
            shop.print_receipt(self)  # Вызов метода print_receipt
            self.location = [12, -2]  # Возвращение домой
            print(f"{self.name} rides home")
            print(f"{self.name} now has {round(self.money, 2)} dollars")
        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop")
