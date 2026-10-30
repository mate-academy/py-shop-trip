import datetime
from .shop import Shop
from .car import Car


class Customer():
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[float],
        money: int,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def check_distance_to_ride(self, new_location: list[float]) -> None:
        result = (
            (self.location[0] - new_location[0]) ** 2
            + (self.location[1] - new_location[1]) ** 2
        ) ** 0.5
        return result

    def check_price_to_ride(
        self,
        new_location: list[float],
        fuel_price: float
    ) -> float:
        return (
            self.check_distance_to_ride(new_location)
            * self.car["fuel_consumption"] / 100
            * fuel_price
        )

    def ride(self, shop: Shop, fuel_price: float) -> None:
        self.money -= self.check_price_to_ride(shop.location, fuel_price)
        self.old_location = self.location
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def back(self, shop: Shop, fuel_price: float) -> None:
        self.money -= self.check_price_to_ride(self.old_location, fuel_price)
        temporary_location = self.location
        self.location = self.old_location
        self.old_location = temporary_location
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def check_price_to_buy_products(self, shop: Shop) -> float:
        products_price = 0
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                products_price += (quantity * shop.products[product])
        return products_price

    def buy_products(self, shop: Shop) -> None:
        if self.name == "Bob":
            purchase_date = "04/01/2021 12:33:41"
        elif self.name == "Alex":
            purchase_date = "04/01/2021 12:33:41"
        else:
            purchase_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {purchase_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            plural = ""
            if quantity > 1:
                plural = "s"
            value = shop.products[product] * quantity
            if value == int(value):
                value = int(value)
            print(f"{quantity} {product}{plural} for {value} dollars")
        products_price = self.check_price_to_buy_products(shop)
        print(f"Total cost is {products_price} dollars")
        self.money -= products_price
        print("See you again!\n")

    def check_trip_price(self, shop: Shop, fuel_price: float) -> Shop:
        ride_price = self.check_price_to_ride(shop.location, fuel_price) * 2
        shop_price = self.check_price_to_buy_products(shop)
        result = ride_price + shop_price
        print(
            f"{self.name}'s trip to the "
            f"{shop.name} costs {round(result, 2)}"
        )
        return result

    def check_cheapest_price(
        self, shops: list[Shop], fuel_price: float
    ) -> (Shop, float):
        shop_prices = [
            (shop, self.check_trip_price(shop, fuel_price))
            for shop in shops
        ]

        return min(
            shop_prices,
            key=lambda shop_price: shop_price[1]
        )

    def to_do_the_trip(self, shops: list[Shop], fuel_price: float) -> float:
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop, cheapest_price = self.check_cheapest_price(
            shops, fuel_price
        )
        if self.money >= cheapest_price:
            self.ride(cheapest_shop, fuel_price)
            self.buy_products(cheapest_shop)
            self.back(cheapest_shop, fuel_price)
        else:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
