from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary.get("name")
        self.product_cart = dictionary.get("product_cart")
        self.location = dictionary.get("location")
        self.money = dictionary.get("money")
        self.car = Car(dictionary.get("car"))

    def trip_cost(self, shop: Shop) -> float:
        products_price = 0
        for product, quantity in self.product_cart.items():
            products_price += quantity * shop.products.get(product)
        money_for_fuel = self.car.fuel_price_for_distance(
            self.location, shop.location
        )
        overheads = products_price + money_for_fuel
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
        products_price = 0
        for product, quantity in self.product_cart.items():
            cur_prod = quantity * shop.products.get(product)
            products_price += cur_prod
            print(
                f"{quantity} {product}s for {cur_prod} dollars"
            )
        print(f"Total cost is {products_price} dollars")
        print("See you again!\n")
        self.money -= (products_price + money_for_fuel)
        print(f"{self.name} rides home")
        self.location = home_location
        print(f"{self.name} now has {self.money} dollars\n")
