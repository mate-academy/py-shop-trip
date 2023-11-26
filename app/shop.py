from dataclasses import dataclass
import datetime

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def calculate_product_cost(self, customer: Customer) -> float:
        total_price = sum(
            quantity * self.products[product]
            for product, quantity in customer.product_cart.items()
        )

        return total_price

    def print_purchase_receipt(self, customer: Customer) -> None:
        actual_dt = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        total_price = self.calculate_product_cost(customer)

        print("\nDate:", actual_dt)
        print(f"Thanks, {customer.name}, for your purchase!\nYou have bought:")

        for product, quantity in customer.product_cart.items():
            price = float(quantity * self.products[product])
            if price.is_integer():
                price = int(price)

            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {total_price} dollars\nSee you again!\n")

    def make_purchase(self, customer: Customer) -> None:
        total_price = self.calculate_product_cost(customer)

        if total_price > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            customer.money -= total_price
            self.print_purchase_receipt(customer)

    def calculate_trip_cost(
            self,
            customer: Customer,
            fuel_price: float
    ) -> float:
        distance_to_shop = customer.calculate_distance(self.location)
        trip_cost = customer.car.calculate_fuel_cost(
            distance_to_shop,
            fuel_price
        )
        products_cost = self.calculate_product_cost(customer)

        return trip_cost + products_cost
