import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def enough_money(self, cost: float) -> bool:
        if self.money < cost:
            print(f"{self} doesn't have enough money "
                  f"to make a purchase in any shop")
            return False
        return True

    def calculate_wallet(self, cost: float) -> float:
        self.money -= cost
        return round(self.money, 2)

    def get_receipts(self, shop: Shop) -> str:
        total_cost = shop.calculate_cart_price(self.product_cart)
        purchase_info = "You have bought:\n"
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                price = shop.products[product]
                cost = float(price * quantity)
                cost = int(cost) if cost.is_integer() else cost
                purchase_info += f"{quantity} {product}s for "
                purchase_info += f"{cost} dollars\n"
        purchase_info += f"Total cost is {total_cost} dollars\nSee you again!"
        return purchase_info

    def costs_for_trip_to_shop(self, shop: Shop, fuel_price: float) -> float:
        return (self._fuel_price(shop.location, fuel_price)
                + shop.calculate_cart_price(self.product_cart))

    def _fuel_price(self, location: list, fuel_price: float) -> float:
        fuel_needed = self._fuel_needed(location, self.car.fuel_consumption)
        return round((fuel_needed * fuel_price) * 2, 2)

    def _fuel_needed(self, location: list, fuel_consumption: float) -> float:
        return (self._calculate_distance(location) * fuel_consumption) / 100

    def _calculate_distance(self, shop_loc: list) -> float:
        return math.dist(self.location, shop_loc)

    def __str__(self) -> str:
        return self.name
