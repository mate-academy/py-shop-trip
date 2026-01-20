from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[float],
        money: float,
        car: Car,
        fuel_price: float,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price

    def make_purchase(self, shops: list[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        trip_total, shop = self.get_cheapest_trip(shops)
        if trip_total <= self.money:
            self.go_shopping(shop)
            print(f"{self.name} now has {round(self.money, 2)} dollars")
            return
        print(
            f"{self.name} doesn't have enough "
            f"money to make a purchase in any shop"
        )

    def get_cheapest_trip(self, shops: list[Shop]) -> tuple[float, Shop]:
        trip_prices: list[tuple[float, Shop]] = []
        for shop in shops:
            car_ride_price: float = (
                self.car.calculate_trip_price(
                    self.fuel_price, self.location, shop.location
                )
                * 2
            )
            shop_total, _ = shop.calculate_total(self.product_cart)
            trip_total: float = car_ride_price + shop_total
            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs {round(trip_total, 2)}"
            )
            trip_prices.append((trip_total, shop))
        return min(trip_prices, key=lambda trip_price: trip_price[0])

    def go_shopping(self, shop: Shop) -> None:
        car_ride_price: float = self.car.calculate_trip_price(
            self.fuel_price, self.location, shop.location
        )

        print(f"{self.name} rides to {shop.name}")
        self.money -= car_ride_price

        receipt: str = shop.purchase_products(self, self.product_cart)
        print(receipt)

        print(f"{self.name} rides home")
        self.money -= car_ride_price
