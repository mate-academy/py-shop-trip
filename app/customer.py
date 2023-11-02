from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self, customer_dict: dict) -> None:
        self.customer_dict = customer_dict
        self._money = self.customer_dict["money"]

    @property
    def name(self) -> str:
        return self.customer_dict["name"]

    @property
    def product_cart(self) -> dict:
        return self.customer_dict["product_cart"]

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, other: int) -> None:
        self._money = other

    @property
    def curr_location(self) -> list[int]:
        return self.customer_dict["location"]

    @curr_location.setter
    def curr_location(self, other: list[int]) -> None:
        self.curr_location = other

    @property
    def home_location(self) -> list[int]:
        return self.customer_dict["location"]

    def calculate_distance(self, shop_coords: list[int]) -> float:
        if len(shop_coords) != 2 or len(self.curr_location) != 2:
            raise ValueError("Coordinates must be 2D [x, y]")

        x1, y1 = self.curr_location
        x2, y2 = shop_coords
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        return distance

    def choose_shop(
            self,
            shops: list[Shop],
            car: Car,
            fuel_price: float
    ) -> Shop | None:
        min_shop = None
        min_total_cost = float("inf")

        for shop in shops:
            price = 0
            for product, quantity in self.product_cart.items():
                if product in shop.product_price:
                    price += shop.product_price[product] * quantity
                else:
                    price = float("inf")
                    break

            fuel_cost = car.get_fuel_price(
                self.calculate_distance(shop.location), fuel_price
            ) * 2
            total_cost = round(price + fuel_cost, 2)

            if total_cost < min_total_cost:
                min_shop = shop
                min_total_cost = total_cost
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        if not self.money < min_total_cost:
            self.money = round(self.money - min_total_cost, 2)
            return min_shop
        else:
            return None
