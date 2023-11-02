from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        money: int | float,
        product_cart: dict,
        location: list[int],
        car_data: dict,
    ) -> None:
        self.name = name
        self.money = money
        self.product_cart = product_cart
        self.location = location
        self.car = Car(car_data["fuel_consumption"])

    def calculate_distance(self, shop_coords: list[int]) -> float:
        if len(shop_coords) != 2 or len(self.location) != 2:
            raise ValueError("Coordinates must be 2D [x, y]")

        x1, y1 = self.location
        x2, y2 = shop_coords
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        return distance

    def choose_shop(self, shops: list[Shop], fuel_price: float) -> Shop | None:
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

            fuel_cost = (
                self.car.get_fuel_price(
                    self.calculate_distance(shop.location), fuel_price
                )
                * 2
            )
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
