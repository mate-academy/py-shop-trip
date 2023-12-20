from __future__ import annotations

from datetime import datetime

# from app.customer import Customer


class Shop:

    def __init__(
            self,
            shop: dict) -> None:
        self._name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def price_count(
            self,
            food_name: str,
            food_amount: int) -> float:
        return round(food_amount * self.products[food_name], 2)

    def customer_buying(
            self,
            customer: callable):

        total_cost = 0

        print("Date: ", datetime.now().strftime("dd/MM/yyyy HH:mm:ss"))
        print(f"Thanks, {self._name}, for your purchase!")
        print("You have bought:")
        for food in customer.product_cart:

            amount_to_byu = customer.product_cart[food]
            food_price = self.price_count(food, amount_to_byu)
            total_cost += food_price

            if amount_to_byu > 1:
                print(f"{customer.product_cart[food]} {food}s for {food_price} dollars")

            if amount_to_byu == 1:
                print(f"1 {food} for {food_price} dollars")

        print(f"Total cost is {total_cost} dollars\nSee you again!")

    @property
    def name(self):
        return self._name
