from math import dist


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def len_trip(location_from: list, location_to: list) -> float:
        return dist(location_from, location_to)

    def cost_trip(
            self,
            customer: object,
            shop: object,
            fuel_price: float) -> float:
        cost = 0
        len_trip = self.len_trip(customer.location, shop.location)
        cost_fuel = round(
            2 * fuel_price * len_trip * self.fuel_consumption / 100, 2
        )

        if shop.is_all_product_in_shop(customer):
            cost = cost_fuel + shop.total_price(customer)

        print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        return cost
