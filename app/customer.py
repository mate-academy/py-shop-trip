from app.shop import Shops
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: int | float,
            car: dict
    ) -> None:
        self.customer_name = name
        self.product_cart = product_cart
        self.customer_location = location
        self.money = money
        self.car = car
        self.customer_home_location = location

    def customers_wallet(self) -> None:
        print(f"{self.customer_name} has {self.money} dollars")

    def customer_shop_trip(
            self,
            shops: list[Shops],
            fuel_price: float,
    ) -> None:

        shop_to_ride = None
        min_price = None
        for shop in shops:
            shops_variants = {}
            distance_of_trip = Car.count_distance(
                customer_location=self.customer_location,
                shop_location=shop.shop_location
            )

            price_in_both_sides = Car.count_amount_full_of_fuel(
                distance=distance_of_trip,
                fuel_consumption=self.car["fuel_consumption"],
                fuel_price=fuel_price
            )

            price_for_products = Shops.count_price_for_products(
                self=shop,
                customer_product_cart=self.product_cart
            )

            full_price = round(price_in_both_sides + price_for_products, 2)

            shops_variants[shop.shop_name] = full_price

            if not min_price or min_price > full_price:
                min_price = full_price
                shop_to_ride = shop

            print(f"{self.customer_name}'s trip to the {shop.shop_name} "
                  f"costs {full_price}")

        if self.money >= min_price:
            print(f"{self.customer_name} rides to {shop_to_ride.shop_name}\n")
            self.customer_location = shop_to_ride.shop_location
            Shops.receipt(
                self=shop_to_ride,
                customer_product_cart=self.product_cart,
                customer_name=self.customer_name
            )
            self.money = self.money - min_price
            Car.go_home(self.customer_name, self.money)
            self.customer_location = self.customer_home_location
        else:
            print(f"{self.customer_name} doesn't have enough money "
                  f"to make a purchase in any shop")
