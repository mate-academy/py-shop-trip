class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def calc_prod_price(self, customer_cart: dict) -> float:
        total = 0
        for item, count in customer_cart.items():
            total += self.products[item] * count
        return total

    def calc_distance(self, customer_location: list) -> float:
        x_delta = self.location[0] - customer_location[0]
        y_delta = self.location[1] - customer_location[1]
        distance = (x_delta**2 + y_delta**2) ** 0.5
        return distance
