from dataclasses import dataclass

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def trip_cost(
            self,
            distance: float | int,
            fuel_price: float | int,
            customer: Customer
    ) -> float | int:
        price = 0
        for product in customer.product_cart:
            price += (self.products.get(product)
                      * customer.product_cart[product])
        return customer.car.fuel_price(distance, fuel_price) * 2 + price

    def print_receipt(self, customer: Customer) -> None:
        customer.location = self.location
        print(f"Date: 04/01/2021 12:33:41\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        cost = 0
        for product, quantity in customer.product_cart.items():
            price = self.products[product] * quantity
            if int(price) == price:
                price = int(price)
            cost += price
            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {cost} dollars\n"
              f"See you again!\n")
