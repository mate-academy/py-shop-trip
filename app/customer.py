from typing import Any


class Customer:
    def __init__(
        self, name: str,
        product_cart: dict,
        location: list[int],
        money: int,
        car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def calculate_trip_price(
            self,
            shop: Any,
    ) -> float:
        if not shop:
            return 0.0

        road_price = self.car.calculate_road_cost(self.location, shop.location)

        products_price = shop.buy_products_cost(**self.product_cart)
        trip_price = road_price + products_price

        return round(trip_price, 2)

    def find_cheapest_trip(
            self,
            shops: list[Any]
    ) -> list[Any]:
        shop_name = ""
        cheapest_trip = float("inf")
        cheapest_shop = None
        money_spend = float("inf")

        for shop in shops:
            trip_price = self.calculate_trip_price(shop)

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {trip_price}"
            )

            if trip_price < cheapest_trip:
                cheapest_trip = trip_price
                shop_name = shop.name
                cheapest_shop = shop
                money_spend = trip_price
        return [shop_name, cheapest_shop, money_spend]
