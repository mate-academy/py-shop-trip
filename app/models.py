
class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_trip_cost(self, distance: float, fuel_price: float) -> float:
        # Витрата пального на 100 км, тому ділимо на 100
        return (distance * self.fuel_consumption / 100) * fuel_price


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_products_cost(self, cart: dict) -> float:
        total = 0.0
        for item, count in cart.items():
            total += count * self.products[item]
        return total
