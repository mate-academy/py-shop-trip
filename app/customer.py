from math import dist
from app.shop import shops_dict


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car_consumption: float) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home = location
        self.location = location
        self.money = money
        self.home = location
        self.car_consumption = car_consumption

    def customer_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def shop_visit(self, shop_name: str, cost: float) -> None:
        print(f"{self.name}'s trip to the {shop_name} costs {cost}")

    def change_location(self, destination: list[int]) -> None:
        self.location = destination

    def come_back_home(self, spent_money: float) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money - spent_money} dollars\n")

    def fuel_cost(self,
                  shop_location: list[int],
                  fuel_price: float) -> float:
        fuel = self.car_consumption / 100
        return fuel * fuel_price * dist(self.location, shop_location)

    def cheapest_shop(self, fuel_price):
        self.customer_info()
        cheapest_shop_price = 1000
        cheapest_shop = None
        for shop in shops_dict.values():
            current_shop = sum(shop.count_product(self.product_cart))
            current_shop += round(
                (self.fuel_cost(shop.location, fuel_price) * 2), 2)
            self.shop_visit(shop.name, current_shop)
            if current_shop < cheapest_shop_price:
                cheapest_shop_price = current_shop
                cheapest_shop = shop

        if cheapest_shop_price <= self.money:
            self.change_location(cheapest_shop.location)
            cheapest_shop.bill(self.name, self.product_cart)
            self.come_back_home(cheapest_shop_price)
            self.change_location(self.home)
        else:
            print(f"{self.name} "
                  f"doesn't have enough money to make a purchase in any shop")