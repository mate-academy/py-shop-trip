class Costumer:
    def __init__(self, costumer_info: dict) -> None:
        self.name = costumer_info["name"]
        self.car = costumer_info["car"]
        self.product_cart = costumer_info["product_cart"]
        self.coords = costumer_info["location"]
        self.money = costumer_info["money"]

    def fuel_cost(self, fuel_price: float) -> float:
        return self.car["fuel_consumption"] * fuel_price / 100
