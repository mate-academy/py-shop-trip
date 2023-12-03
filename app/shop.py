from datetime import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    fuel_price: float | int
    name: str
    location: list
    products: dict
    cost_of_trip: float | None = None

    def get_cost_for_travel(self,
                            customer_location: list,
                            customer_car: dict) -> float | int:
        distance = ((customer_location[0] - self.location[0]) ** 2
                    + (customer_location[1] - self.location[1]) ** 2) ** 0.5
        cost_for_travel = round(((distance / 100)
                                 * customer_car["fuel_consumption"]
                                 * self.fuel_price * 2), 2)
        return cost_for_travel

    def cost_of_product(self, product: str, amount: int) -> float | int:
        return self.products[product] * amount

    def get_products_cost(self, customer_product_cart: dict) -> float | int:
        total_cost = 0
        for product, amount in customer_product_cart.items():
            total_cost += self.cost_of_product(product, amount)
        return total_cost

    def get_cost_of_trip(self,
                         cust_prod_cart: dict,
                         cust_loc: list,
                         cust_car: dict) -> None:
        self.cost_of_trip = (self.get_products_cost(cust_prod_cart)
                             + self.get_cost_for_travel(cust_loc, cust_car))

    def print_receipt(self,
                      customer_name: str,
                      customer_product_cart: dict) -> None:
        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {today}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought: ")

        for product, amount in customer_product_cart.items():
            products_cost = self.cost_of_product(product, amount)
            products_cost = (int(products_cost) if
                             int(products_cost) == products_cost
                             else products_cost)
            print(f"{amount} {product}s for {products_cost} dollars")
        print(f"Total cost is {self.get_products_cost(customer_product_cart)}"
              f" dollars\nSee you again!\n")
