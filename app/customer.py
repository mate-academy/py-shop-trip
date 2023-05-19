from dataclasses import dataclass
from app.shop import Shop
from datetime import datetime


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int | float
    car: dict

    def product_price(self, shop: Shop) -> int | float:
        return sum(
            self.product_cart[product] * shop.products[product]
            for product in shop.products.keys()
        )

    def distance_price(self, shop: Shop, fuel_price: int | float) -> float:
        dist = ((shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2) ** 0.5

        price_per_liter = self.car["fuel_consumption"] / 100 * fuel_price
        total_dist_cost = (dist * price_per_liter) * 2
        return round(total_dist_cost, 2)

    def find_min_cost_shop(self,
                           shops: list[Shop],
                           fuel_price: int | float) -> Shop:
        min_cost = float("inf")
        min_shop = None

        for shop in shops:
            dist_price = self.distance_price(shop, fuel_price)
            prod_price = self.product_price(shop)
            total_cost = dist_price + prod_price
            if (total_cost <= self.money
                    and (min_shop is None or total_cost < min_cost)):
                min_cost = total_cost
                min_shop = shop
        return min_shop

    def trip(self, shops: list[Shop], fuel_price: int | float) -> None:
        start_location = self.location
        cheapest_location = self.find_min_cost_shop(shops, fuel_price)
        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            dist_price = self.distance_price(shop, fuel_price)
            prod_price = self.product_price(shop)
            total_cost = dist_price + prod_price
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        if cheapest_location is None:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        else:
            print(f"{self.name} rides to {cheapest_location.name}\n")
            self.money -= self.distance_price(cheapest_location, fuel_price)
            self.location = cheapest_location.location
        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")

        for product in cheapest_location.products:
            each_prod_price = (cheapest_location.products[product]
                               * self.product_cart[product])
            print(f"{self.product_cart[product]} {product}s "
                  f"for {each_prod_price} dollars")
        print(f"Total cost is {self.product_price(cheapest_location)} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        self.money -= self.product_price(cheapest_location)
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        self.location = start_location
