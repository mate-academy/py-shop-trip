from app.car import Car
from app.shop import Shop
import datetime


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def __str__(self) -> str:
        return (f"Customer(name={self.name}, "
                f"product_cart={self.product_cart}, "
                f"location={self.location}, "
                f"money={self.money}, car={self.car})")

    def calculate_distance(self, other_location: list) -> float:
        return ((self.location[0] - other_location[0]) ** 2
                + (self.location[1] - other_location[1]) ** 2) ** 0.5

    def cost_of_products(self, price: dict) -> float:
        return sum(self.product_cart[product] * price[product]
                   for product in self.product_cart)

    def calculate_trip_expenses(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> float:
        return round(self.calculate_distance(shop.location)
                     * self.car.fuel_consumption * fuel_price * 2 / 100
                     + self.cost_of_products(shop.products), 2)

    def shopping(self, shop: Shop) -> None:
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {formatted_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        spending_on_products = 0
        for product in self.product_cart:
            purchase = self.product_cart[product] * shop.products[product]
            str_purchase = int(purchase) \
                if purchase == int(purchase) \
                else purchase
            spending_on_products += purchase
            print(f"{self.product_cart[product]} {product}s for "
                  f"{str_purchase} dollars")
        print(f"Total cost is {spending_on_products} dollars")
        print("See you again!\n")
