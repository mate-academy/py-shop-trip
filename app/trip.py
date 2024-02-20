from __future__ import annotations


class Trip:

    def __init__(
            self,
            shop_name: str,
            trip_price: float,
            total_milk_cost: float,
            total_bread_cost: float,
            total_butter_cost: float
    ) -> None:
        self.shop_name = shop_name
        self.trip_price = trip_price
        self.total_milk_cost = total_milk_cost
        self.total_bread_cost = total_bread_cost
        self.total_butter_cost = total_butter_cost
        self.total_product_price = sum(
            [total_milk_cost, total_bread_cost, total_butter_cost]
        )
        self.total_trip = self.trip_price + self.total_product_price

    @staticmethod
    def cheapest_trip(trips: list) -> Trip:
        return min(trips, key=lambda obj: obj.total_trip)
