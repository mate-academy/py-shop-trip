import datetime
from app.shop import Shop
from typing import List
from app.car import distance


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def cost_of_products(self, shop: Shop) -> int:
        total_cost = 0
        for product, num in self.product_cart.items():
            cost = shop.products[product] * num
            total_cost += cost
        return total_cost

    def purchase_receipt(self, shop: Shop) -> None:
        total_cost = 0
        current_date = datetime.datetime.now()
        print(f"Date: {current_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        for product, num in self.product_cart.items():
            cost = shop.products[product] * num
            print(f"{num} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def shopping(self, shops: List[Shop], fuel_price: float) -> None:
        shop_dict = {}
        for shop in shops:
            products_cost = self.cost_of_products(shop)
            shop_distance = distance(self.location, shop.location)
            car_cost = 2 * shop_distance * \
                self.car["fuel_consumption"] / 100 * fuel_price
            trip_cost = round((car_cost + products_cost), 2)
            shop_dict[trip_cost] = shop
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {trip_cost}")
        min_trip_cost = min(shop_dict.keys())
        suitable_shop = shop_dict[min_trip_cost]
        if self.money <= min_trip_cost:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            self.money -= min_trip_cost
            print(f"{self.name} rides to {suitable_shop.name}\n")
            self.purchase_receipt(suitable_shop)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money} dollars\n")
