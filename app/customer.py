class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def cost_trip(self, fuel_price: float, shop_location: list) -> float:
        dist_len = ((((self.location[1] - shop_location[1]) ** 2)
                     + ((self.location[0] - shop_location[0]) ** 2)) ** 0.5)
        cost_trip = round((((dist_len * self.car["fuel_consumption"]) / 100)
                           * fuel_price * 2), 2)
        return cost_trip
