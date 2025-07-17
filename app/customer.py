from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
    ) -> None:
        self.name = name
        self.money = money
        self.location = location
        self.product_cart = product_cart

    def start_customer(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def trips_costs(self, shop: Shop, result_cost: float) -> None:
        return f"{self.name}'s trip to the {shop.name} costs {result_cost}"

    def start_ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")

    def end_trip(self, full_prices: float | int) -> None:
        self.money -= full_prices
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
