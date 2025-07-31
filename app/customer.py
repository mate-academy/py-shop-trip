from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = location
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_dict(cls, data: dict) -> list["Customer"]:
        return [
                cls(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(customer["car"]["brand"],
                        customer["car"]["fuel_consumption"])
                ) for customer in data
        ]

    def calculate_distance(self, shop: Shop) -> float:
        return round(((shop.location[0] - self.location[0]) ** 2
                      + (shop.location[1] - self.location[1]) ** 2) ** 0.5, 2)

    def calculate_price_of_products(self, shop: Shop) -> float:
        _sum = 0
        for product in self.product_cart:
            _sum += self.product_cart[product] * shop.products[product]

        return round(_sum, 2)

    def calculate_price_of_shop_trip(self, shop: Shop,
                                     fuel_price: float) -> float:
        return (round(
            self.calculate_price_of_products(shop)
            + self.car.calculate_price_of_trip(self.calculate_distance(shop),
                                               fuel_price), 2))

    def calculate_cheapest_trip(self, shops: list[Shop],
                                fuel_price: float) -> (float, Shop):
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop_price = float("inf")
        current_shop = None
        for shop in shops:
            current_shop_price = self.calculate_price_of_shop_trip(shop,
                                                                   fuel_price)
            if current_shop_price < cheapest_shop_price:
                cheapest_shop_price = current_shop_price
                current_shop = shop
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {current_shop_price}")

        return current_shop, cheapest_shop_price

    def make_trip_to_shop(self, shop: Shop, shop_price: float) -> bool:
        if self.money >= shop_price:
            print(f"{self.name} rides to {shop.name}\n")
            self.location = shop.location
            self.money = round(self.money - shop_price, 2)

            return True

        print(f"{self.name} doesn't have enough money"
              f" to make a purchase in any shop")
        return False

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        print(f"{self.name} now has {self.money} dollars\n")
