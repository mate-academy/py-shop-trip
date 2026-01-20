from typing import List, Dict
from app.customer import Customer


class Shop:
    def __init__(self, name: str,
                 location: List[int],
                 products: Dict[str, float]
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_distance_to_shop(self, customer: Customer) -> float:
        return ((self.location[0] - customer.location[0]) ** 2
                + (self.location[1] - customer.location[1]) ** 2) ** 0.5

    def calculate_cost_products(self, customer: Customer) -> float:
        return sum(customer.product_cart[product] * price
                   for product, price in self.products.items())

    def trip_calculation(self, customer: Customer, fuel_price: float) -> float:
        distance = self.cost_distance_to_shop(customer=customer)
        fuel_consumption = customer.car["fuel_consumption"]

        return (distance * fuel_consumption * fuel_price * 2) / 100

    def total_costing(self, customer: Customer, fuel_price: float) -> float:
        products = self.calculate_cost_products(customer=customer)
        trip = self.trip_calculation(customer=customer, fuel_price=fuel_price)

        return round(products + trip, 2)

    def basket_collection(self, customer: Customer) -> dict:
        return {
            product: [
                customer.product_cart[product],
                customer.product_cart[product] * price
            ]
            for product, price in self.products.items()
        }
