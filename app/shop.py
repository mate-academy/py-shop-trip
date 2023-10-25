from datetime import datetime
from calculate_distance import calculate_distance


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_purchase_cost(self, customer_cart: dict) -> float:
        total_cost = 0
        for item, quantity in customer_cart.items():
            if item in self.products:
                total_cost += quantity * self.products[item]
        return total_cost

    def print_receipt(
            self,
            customer_name: str,
            customer_cart: dict,
            purchase_cost: float
    ) -> None:
        current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for item, quantity in customer_cart.items():
            if item in self.products:
                cost = quantity * self.products[item]
                print(f"{quantity} {item}s for {cost} dollars")
        print(f"Total cost is {purchase_cost} dollars")
        print("See you again!")

    def calculate_distance_to_customer(self, customer_location: list) -> float:
        distance = calculate_distance(self.location, customer_location)
        return distance

    def get_location(self) -> list:
        return self.location
