from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary["name"]
        self.product_cart = dictionary["product_cart"]
        self.location = dictionary["location"]
        self.money = dictionary["money"]
        self.car = Car(dictionary["car"])

    def trip_cost(self, shop: Shop) -> float:
        products_price = self.receipt(shop)
        money_for_fuel = self.car.fuel_price_for_distance(
            self.location, shop.location
        )
        overheads = sum(products_price.values()) + money_for_fuel
        print(f"{self.name}'s trip to the {shop.name} costs {overheads}")
        return overheads

    def purchase(self, shop: Shop) -> None:
        home_location = self.location
        money_for_fuel = self.car.fuel_price_for_distance(
            self.location, shop.location
        )
        self.location = shop.location
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        products_price = self.receipt(shop)
        for product, quantity in self.product_cart.items():
            print(
                f"{quantity} {product}s for {products_price[product]} dollars"
            )
        print(f"Total cost is {sum(products_price.values())} dollars")
        print("See you again!\n")
        self.money -= (sum(products_price.values()) + money_for_fuel)
        print(f"{self.name} rides home")
        self.location = home_location
        print(f"{self.name} now has {self.money} dollars\n")

    def receipt(self, shop: Shop) -> dict:
        purchase_receipt = {}
        for product, quantity in self.product_cart.items():
            purchase_receipt[product] = quantity * shop.products[product]
        return purchase_receipt
