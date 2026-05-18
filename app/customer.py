from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: int,
            car: dict[str, str | float]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = float(money)
        self.car = Car(**car)

    def get_distance(self, location: list[int]) -> float:
        return (
            (location[0] - self.location[0]) ** 2
            + (location[1] - self.location[1]) ** 2
        ) ** 0.5

    def fuel_cost_for_trip(self, shop: Shop, fuel_cost: float) -> float:
        distance = self.get_distance(shop.location) * 2
        fuel_car = distance / 100 * self.car.fuel_consumption
        return fuel_car * fuel_cost

    def trip_costs(
            self,
            shops: list[Shop],
            fuel_cost: float
    ) -> list[dict[str, str | Shop | float | dict[str, float]]]:
        result = []
        for shop in shops:
            cost_of_product = shop.cost_of_products(self.product_cart)
            cost_of_distance = self.fuel_cost_for_trip(shop, fuel_cost)
            total_cost = round(
                sum(cost_of_product.values()) + cost_of_distance,
                2
            )
            result.append(
                {
                    "shop_name": shop.name,
                    "cost": total_cost,
                    "shop_obj": shop,
                    "products": cost_of_product,
                }
            )
        return result
