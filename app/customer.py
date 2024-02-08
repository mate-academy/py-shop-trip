import math

from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.total_expenses_for_every_shop = {}
        self.best_shop = {}

    def cost_to_drive_to_shop_and_back(
            self,
            shop_location: list,
            fuel_cost: float
    ) -> float:
        distance_to_shop = math.sqrt(
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        )
        consumption_per_km = self.car["fuel_consumption"] / 100
        return round(
            2 * distance_to_shop * consumption_per_km * fuel_cost, 2
        )

    def cost_of_all_products_to_buy(
            self,
            shops_products: dict,
    ) -> float:
        total_cost = 0
        for product, quantity in self.product_cart.items():
            cost_of_product = quantity * shops_products[product]
            total_cost += cost_of_product
        return total_cost

    def calculate_total_expenses(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> None:
        for shop in shops:
            self.total_expenses_for_every_shop[shop] = (
                self.cost_to_drive_to_shop_and_back(shop.location, fuel_price)
                + self.cost_of_all_products_to_buy(shop.products)
            )

    def choose_shop_with_minimal_expenses(self) -> None:
        self.best_shop = min(
            self.total_expenses_for_every_shop,
            key=self.total_expenses_for_every_shop.get
        )
        self.best_shop = {
            self.best_shop: self.total_expenses_for_every_shop[self.best_shop]
        }
