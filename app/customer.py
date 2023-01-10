from app.shop import Shop
import datetime


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def fuel_cost_for_trip(self, cost_per_liter: float, shop: Shop) -> float:
        coast = (
            self.car["fuel_consumption"]
            * self.distance_to_shop(shop)
            * cost_per_liter / 100
        )
        return coast

    def distance_to_shop(self, shop: Shop) -> float:
        distance = (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5
        return distance

    def cost_of_trip_to_shop(
            self,
            shop: Shop,
            cost_per_liter: float
    ) -> float:
        total_cost = self.fuel_cost_for_trip(cost_per_liter, shop) * 2
        for product in self.product_cart:
            total_cost += self.product_cart[product] * shop.products[product]
        return round(total_cost, 2)

    def go_shopping(self, shop: Shop, cost_per_liter: float) -> None:
        customer_home = self.location.copy()
        print(f"{self.name} rides to {shop.name}")
        spend_money = self.cost_of_trip_to_shop(shop, cost_per_liter)
        print()
        self.location = shop.location
        data_of_purchase = (
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
        print(f"Date: {data_of_purchase}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_cost_of_products = 0
        for product in self.product_cart:
            cost_of_product = (
                self.product_cart[product] * shop.products[product]
            )
            print(
                f"{self.product_cart[product]} {product}s for"
                f" {cost_of_product} dollars"
            )
            total_cost_of_products += (
                self.product_cart[product] * shop.products[product]
            )
        print(f"Total cost is {total_cost_of_products} dollars")
        self.money -= spend_money
        print("See you again!\n")
        print(f"{self.name} rides home")
        self.location = customer_home
        print(f"{self.name} now has {self.money} dollars\n")
