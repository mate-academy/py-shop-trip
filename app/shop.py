from math import sqrt
from datetime import datetime


class Shop:
    def __init__(self, name: str, location: tuple, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_trip_cost(
            self,
            customer_location: tuple,
            fuel_price: float,
            fuel_consumption: float
    ) -> tuple:
        distance = sqrt((self.location[0] - customer_location[0]) ** 2
                        + (self.location[1] - customer_location[1]) ** 2)
        return round(
            distance * 2 * fuel_consumption / 100 * fuel_price, 2
        ), distance

    def purchase(self, customer_name: str, product_cart: dict) -> tuple:
        total_cost = 0
        specific_time = datetime.now()  # Get current time
        receipt = [
            f"Date: {specific_time.strftime("%m/%d/%Y %H:%M:%S")}",
            f"Thanks, {customer_name}, for your purchase!",
            "You have bought:"
        ]

        for product, quantity in product_cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                formatted_cost = int(cost) \
                    if cost.is_integer() \
                    else round(cost, 1)
                receipt.append(f"{quantity} {product}s "
                               f"for {formatted_cost} dollars")
                total_cost += cost

        total_cost = int(total_cost) if total_cost.is_integer() \
            else round(total_cost, 1)
        receipt.append(f"Total cost is {total_cost} dollars")
        receipt.append("See you again!\n")

        return total_cost, "\n".join(receipt)
