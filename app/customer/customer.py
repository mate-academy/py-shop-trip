from datetime import datetime
from typing import List, Dict
from app.shop.shop import Shop


class NotEnoughMoney(Exception):
    """If customer doesn't have enough money"""


class Customer:
    def __init__(self, customer: dict):
        self._name = customer['name']
        self._product_cart = customer['product_cart']
        self._location = customer['location']
        self._money = customer['money']
        self._car = customer['car']

    def trip(self, shops_list: List[Shop], fuel_price: float):
        print(f'{self._name} has {self._money} dollars')
        trip_cost = {}
        current_shop_by_name = {}

        for iterator, shop in enumerate(shops_list):
            cost_products = self.calculate_product(shop)
            cost_trip = self.calculate_trip(
                shop.location,
                fuel_price,
                self._car['fuel_consumption']
            )
            trip_cost[shop.name] = round(cost_trip + cost_products, 2)
            current_shop_by_name[shop.name] = shop

            print(f"{self._name}'s trip to the {shop.name}"
                  f" costs {trip_cost[shop.name]}")

        try:
            minimal_cost = self.calculate_cheapest_ride(trip_cost)
        except NotEnoughMoney:
            print(f"{self._name} doesn't have enough money"
                  f" to make purchase in any shop")
            return

        print(f"{self._name}'s rides to {minimal_cost['name']}")

        for shop in current_shop_by_name:
            # Find required shop and ride
            if shop == minimal_cost["name"]:
                home_location = self._location

                self.riding_to_shop(current_shop_by_name[shop])
                self._location = home_location
                __money_left = self._money - minimal_cost["cost"]
                print(f"{self._name} now has {__money_left} dollars\n")
                break

    def riding_to_shop(self, shop: Shop):
        date_today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        self._location = shop.location

        _cost_milk = self._product_cart["milk"] * shop.products["milk"]
        _cost_bread = self._product_cart["bread"] * shop.products["bread"]
        _cost_butter = self._product_cart["butter"] * shop.products["butter"]
        _total_cost = _cost_butter + _cost_milk + _cost_bread

        print()
        print(f"Date: {date_today}")
        print(f"Thanks, {self._name}, for you purchase!")
        print("You have bought:")
        print(f"{self._product_cart['milk']} milks for {_cost_milk} dollars")

        print(f"{self._product_cart['bread']} breads for"
              f" {_cost_bread} dollars")
        print(f"{self._product_cart['butter']} butters for"
              f" {_cost_butter} dollars")

        print(f"Total cost is {_total_cost} dollars")
        print("See you again!\n")

        print(f"{self._name} rides home")
        return _total_cost

    def calculate_cheapest_ride(
            self,
            rides_price: Dict[str, float]
    ) -> Dict[str, str]:
        cheapest = float("inf")
        riding_shop = {}

        for name, cost in rides_price.items():
            if cost < cheapest and self._money > cost:
                riding_shop["name"] = name
                riding_shop["cost"] = cost
                cheapest = cost

        if riding_shop:
            return riding_shop
        raise NotEnoughMoney()

    def calculate_product(self, shop: Shop) -> float:
        cost = 0

        for product, price in shop.products.items():
            cost += self._product_cart[product] * price

        return cost

    def calculate_trip(
            self,
            shop_location: List[int],
            fuel_price: float,
            fuel_consumption: float
    ) -> float:
        cost_location_x = round((self._location[0] - shop_location[0]) ** 2, 2)
        cost_location_y = round((self._location[1] - shop_location[1]) ** 2, 2)
        distance_price = round((cost_location_x + cost_location_y) ** 0.5, 2)
        total_cost = (fuel_consumption * distance_price) / 100

        return round(total_cost * fuel_price, 2)
