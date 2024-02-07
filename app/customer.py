from app.shop import Shop
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

    def show_customers_wallet(self) -> None:
        print(f"{self.customer_name} has {self.money} dollars")

    def customer_shop_trip(
            self,
            shops: list[Shop],
            fuel_price: float,
    ) -> None:
        shop_to_ride, min_price = self.find_cheapest_shop(shops, fuel_price)

        if shop_to_ride is not None and self.money >= min_price:
            self.make_trip_to_shop(shop_to_ride)
            self.process_shopping_in_shop(shop_to_ride, min_price)
            self.go_back_home()
        else:
            print(f"{self.customer_name} doesn't have enough money "
                  "to make a purchase in any shop")

    def find_cheapest_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> tuple:
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

            price_for_products = Shop.count_price_for_products(
                self=shop,
                customer_product_cart=self.product_cart
            )

            full_price = round(price_in_both_sides + price_for_products, 2)
            shops_variants[shop.shop_name] = full_price

            print(f"{self.customer_name}'s trip to the {shop.shop_name} "
                  f"costs {full_price}")

            if not min_price or min_price > full_price:
                min_price, shop_to_ride = full_price, shop

        return shop_to_ride, min_price

    def make_trip_to_shop(self, shop: Shop) -> None:
        print(f"{self.customer_name} rides to {shop.shop_name}\n")
        self.customer_location = shop.shop_location

    def process_shopping_in_shop(
            self,
            shop: Shop,
            min_price: int | float
    ) -> None:
        Shop.receipt(
            self=shop,
            customer_product_cart=self.product_cart,
            customer_name=self.customer_name
        )
        self.money = self.money - min_price

    def go_back_home(self) -> None:
        Car.go_home(self.customer_name, self.money)
        self.customer_location = self.customer_home_location
