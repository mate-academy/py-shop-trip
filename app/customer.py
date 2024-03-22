from app.car import Car


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int | float,
                 car: dict) -> None:
        self.name = name
        self.products = product_cart
        self.location = location
        self.money = money
        self.car = car["fuel_consumption"]

    def calculate_trip_cost(self, shop: object,
                            fuel_price: int | float
                            ) -> int | float:
        fuel_cost_to = Car(self.car, fuel_price, shop, self.location)
        total_cost = fuel_cost_to.calculate_fuel_cost()
        for product in shop.products:
            if product in self.products:
                total_cost += (shop.products[product] * self.products[product])
        return round(total_cost, 2)

    def update_location(self, new_location: list) -> None:
        self.location = new_location
