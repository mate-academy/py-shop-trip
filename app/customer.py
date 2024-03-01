from app.car import Car


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data.get("name")
        self.product_cart = data.get("product_cart", {})
        self.location = data.get("location", [])
        self.home_location = data.get("location", [])
        self.money = data.get("money")
        self.best_shop = None

        car_data = data.get("car")
        self.car = Car(**car_data)
