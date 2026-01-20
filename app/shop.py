from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_total_cost(self, product_cart: dict) -> float:
        total = 0.0
        for product, quantity in product_cart.items():
            if product in self.products:
                total += self.products[product] * quantity
        return total

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print(
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                total_cost += cost
                cost_str = f"{cost:.1f}" if cost % 1 else f"{int(cost)}"
                print(f"{quantity} {product}s for {cost_str} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")


# Bob has 55 dollars
# Bob's trip to the Outskirts Shop costs 28.21
# Bob's trip to the Shop '24/7' costs 31.48
# Bob rides to Outskirts Shop
#
# Date: 04/01/2021 12:33:41
# Thanks, Bob, for your purchase!
# You have bought:
# 4 milks for 12 dollars
# 2 breads for 2 dollars
# 5 butters for 12.5 dollars
# Total cost is 26.5 dollars
# See you again!
#
# Bob rides home
# Bob now has 26.79 dollars
#
# Monica has 12 dollars
# Monica's trip to the Outskirts Shop costs 15.65
# Monica's trip to the Shop '24/7' costs 16.84
# Monica doesn't have enough money to make a purchase in any shop
