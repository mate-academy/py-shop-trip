from __future__ import annotations


class Shop:

    def __init__(
            self,
            shop: dict) -> None:
        self._name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def customer_buying(
            self,
            customer: callable):

        total_cost = 0

        # print("Date: ", datetime.now().strftime("%d/%m/%y %H:%M:%S"))
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer._name}, for your purchase!")
        print("You have bought:")
        for food in customer.product_cart:

            amount = customer.product_cart[food]
            food_price = round(amount * self.products[food], 2)

            if food_price % 1 == 0:
                food_price = int(food_price)
            total_cost += food_price

            if amount > 1:
                print(f"{customer.product_cart[food]} {food}s for {food_price} dollars")

            if amount == 1:
                print(f"1 {food} for {food_price} dollars")

        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
