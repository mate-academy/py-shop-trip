class Customer:
    def __init__(self, customers: dict) -> None:
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]

    def cost_trip(self, fuel_price: float, shop_location: list):
        dist_len = ((((self.location[1] - shop_location[1]) ** 2)
                     + ((self.location[0] - shop_location[0]) ** 2)) ** 0.5)
        cost_trip = round((((dist_len * self.car["fuel_consumption"]) / 100)
                           * fuel_price * 2), 2)
        return cost_trip
