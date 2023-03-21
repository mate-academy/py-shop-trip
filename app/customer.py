from app.car import Car
from app.shop import Shop
import datetime


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name = customer_info["name"]
        self.product_cart = customer_info["product_cart"]
        self.location = customer_info["location"]
        self.money = customer_info["money"]
        self.car = Car(customer_info["car"])

    def calculate_fuel_cost(
            self,
            shop_location: list[int],
            fuel_price: float
    ) -> float:
        distance = (
            ((self.location[0] - shop_location[0]) ** 2
             + (self.location[1] - shop_location[1]) ** 2) ** 0.5
        )
        fuel_cost = self.car.fuel_consumption * distance / 100 * fuel_price

        return fuel_cost * 2

    def calculate_products_cost(self, products_in_shop: dict) -> float:
        product_cost = 0
        for product, amount in self.product_cart.items():
            product_cost += products_in_shop[product] * amount
        return product_cost

    def select_shop(
            self,
            fuel_price: float,
            shop_list: list[Shop]
    ) -> tuple[Shop, dict]:
        list_expenses = []

        for shop in shop_list:
            expenses = {
                "fuel": round(
                    self.calculate_fuel_cost(shop.location, fuel_price), 2
                ),
                "product": round(
                    self.calculate_products_cost(shop.products), 2
                )
            }
            expenses["total"] = sum(expenses.values())
            list_expenses.append(expenses)

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {expenses['total']}")

        list_total_expenses = [sum(x.values()) for x in list_expenses]
        index = list_total_expenses.index(min(list_total_expenses))
        selected_shop = shop_list[index]

        return selected_shop, list_expenses[index]

    def go_to_shop(self, shop: Shop, expenses: dict) -> None:
        self.location = shop.location

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %X')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in self.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{shop.products[product] * amount} dollars")

        print(f"Total cost is {expenses['product']} dollars")
        print("See you again!\n")

        self.money -= expenses["total"]

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
