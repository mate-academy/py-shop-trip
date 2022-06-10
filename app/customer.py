from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int, car: Car):
        self.name = name
        self.product_cart = product_cart
        self.location_x = location[0]
        self.location_y = location[1]
        self.money = money
        self.car = car

    def count_trip_price(self, shop: Shop, fuel_price: float):
        x_difference = self.location_x - shop.location_x
        y_difference = self.location_y - shop.location_y
        distance = (x_difference ** 2 + y_difference ** 2) ** 0.5

        price_for_1km = (self.car.fuel_consumption / 100) * fuel_price

        return distance * price_for_1km

    def count_purchase_price(self, shop: Shop):
        result = 0.0

        for product, number in self.product_cart.items():
            if product in shop.products:
                result += number * shop.products[product]

        return result

    def total_price(self, shop: Shop, fuel_price: float):
        total_trip_price = self.count_trip_price(shop, fuel_price) * 2
        total_purchase_price = self.count_purchase_price(shop)
        return total_trip_price + total_purchase_price

    def choose_cheapest_trip(self, shops_list: list[Shop], fuel_price):
        result = None
        best_price = self.money

        print(f"{self.name} has {self.money} dollars")

        for shop in shops_list:
            total_price = self.total_price(shop, fuel_price)
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {round(total_price, 2)}")

            if total_price < best_price:
                result = shop
                best_price = total_price

        if result is None:
            print(f"{self.name} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            print(f"{self.name} rides to {result.name}\n")

        return result

    def go_home(self):
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def pay(self, price: float):
        self.money -= price

    def change_location(self, new_location_x: int, new_location_y: int):
        self.location_x = new_location_x
        self.location_y = new_location_y
