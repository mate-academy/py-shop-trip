from app.car import Car


class Customer:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.product_cart = config["product_cart"]
        self.money = config["money"]
        self.home_location = config["location"]
        self.location = config["location"]
        car_data = config.get("car", {})
        self.car = Car(
            car_data["brand"],
            car_data["fuel_consumption"]
        )

    def go_to(self, new_location: list) -> None:
        self.location = new_location

    def return_home(self) -> None:
        self.location = self.home_location

    def calculate_total_costs(self, shops: list, fuel_price: float) -> list:
        costs = []
        for shop in shops:
            fuel_cost = self.car.cost_fuel(
                self.location, shop.location, fuel_price
            )
            products_cost = shop.cost_of_products(self.product_cart)
            total = fuel_cost + products_cost
            costs.append((shop, round(total, 2)))
        return costs
