class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            home_location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = home_location
        self.money = money

        self.car_brand = car["brand"]
        self.car_fuel_consumption = car["fuel_consumption"]

        self.current_location = home_location
        self.has_enough_money = False
        self.chosen_shop = None
        self.fuel_cost_to_destination = None
