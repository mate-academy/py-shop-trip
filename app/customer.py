class Customer:
    def __init__(
            self, name: str, product_cart: dict,
            location: list, money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location

    def customer_choice(self, trip_cost: float, shop_name: str) -> None:
        if trip_cost > self.money:
            print(
                f"{self.name} doesn't have enough"
                f" money to make a purchase in any shop"
            )
        else:
            print(f"{self.name} rides to {shop_name}")
