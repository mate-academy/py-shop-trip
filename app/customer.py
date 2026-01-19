from typing import Any
from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self,
                 client_name: str,
                 client_products: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.client_name = client_name
        self.client_products = client_products
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def total_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.car.calculate_distance(self.location, shop.location)
        fuel_cost = self.car.fuel_cost(distance * 2, fuel_price)
        product_cost = shop.products_cost(self.client_products)
        return fuel_cost + product_cost

    def right_store(self, shops: list, fuel_price: float) -> Any:
        best_cost = float("inf")
        best_shop = None
        for shop in shops:
            total_cost = self.total_cost(shop, fuel_price)
            print(f"{self.client_name}'s trip to the "
                  f"{shop.name} costs {round(total_cost, 2)}")
            if 0 < total_cost < best_cost:
                best_cost = total_cost
                best_shop = shop
        if self.money > best_cost:
            print(f"{self.client_name} rides to {best_shop.name}\n")
        return best_shop, best_cost

    def trip_or_stay_home(self, shop: Shop, fuel_price: float) -> None:
        total_cost = self.total_cost(shop, fuel_price)
        product_cost = shop.products_cost(self.client_products)
        if self.money > total_cost:
            self.money -= total_cost
            self.location = shop.location
            shop.purchase_receipt(self.client_name,
                                  self.client_products,
                                  product_cost)
            print(f"\n{self.client_name} rides home")
            print(f"{self.client_name} now has"
                  f" {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.client_name} doesn't have enough"
                  f" money to make a purchase in any shop")
