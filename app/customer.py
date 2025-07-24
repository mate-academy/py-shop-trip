from app.car import Car
from app.shop import Shop
from app.utils import round_to_2


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name: str = customer_info["name"]
        self.product_cart: dict = customer_info["product_cart"]
        self.location: list[int] = customer_info["location"]
        self.home_location = self.location.copy()
        self.money: int | float = customer_info["money"]
        self.car: Car = Car(customer_info["car"])

    def _calculate_fuel_cost(
            self,
            fuel_price: int | float,
            shop_location: list[int]
    ) -> int | float:
        distance = ((shop_location[0] - self.location[0]) ** 2
                    + (shop_location[1] - self.location[1]) ** 2) ** 0.5
        return fuel_price * (self.car.fuel_consumption * distance / 100) * 2

    def _calculate_products_cost(
            self, products: dict) -> int | float:
        return sum(
            products.get(product, 0) * quantity
            for product, quantity in self.product_cart.items()
        )

    def calculate_trip_cost(
            self,
            fuel_price: float,
            shop: Shop
    ) -> int | float:
        product_cost = self._calculate_products_cost(shop.products)
        fuel_cost = self._calculate_fuel_cost(fuel_price, shop.location)
        trip_cost = round_to_2(product_cost + fuel_cost)
        print(f"{self.name}'s trip to the "
              f"{shop.name} costs {trip_cost}")
        return trip_cost

    def go_shopping(self, shop: Shop, spending: int | float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location.copy()
        shop.print_receipt(self.name, self.product_cart)
        self.money -= spending

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location.copy()
        print(f"{self.name} now has {self.money} dollars\n")
