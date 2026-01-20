from app.protocol import CarProtocol, ShopProtocol


class Customer:
    def __init__(self, name: str,
                 product_cart: dict[str, int],
                 location: list[int],
                 money: int,
                 car: CarProtocol) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calc_trip_cost(self,
                       shop: ShopProtocol,
                       fuel_price: float) -> float:
        x_home, y_home = self.location
        x_shop, y_shop = shop.location
        distance = ((x_shop - x_home) ** 2 + (y_shop - y_home) ** 2) ** 0.5
        total_distance = distance * 2
        liters = (self.car.fuel_consumption * total_distance) * 0.01
        fuel_cost = liters * fuel_price
        total_for_products = 0
        for product, amount in self.product_cart.items():
            total_for_products += shop.products[str(product)] * amount
        total_for_trip = total_for_products + fuel_cost
        return round(total_for_trip, 2)
