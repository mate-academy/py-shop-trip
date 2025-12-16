from math import dist
from app.shop import Shop


class Customer:
    def __init__(self, person_dict: dict) -> None:
        self.name = person_dict["name"]
        self.product_cart = person_dict["product_cart"]
        self.coords = person_dict["location"]
        self.money = person_dict["money"]
        self.fuel_for_1_km = person_dict["car"]["fuel_consumption"] / 100

    def fuel_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(dist(
            shop.coords, self.coords
        ) * self.fuel_for_1_km * fuel_price * 2, 2)

    def trip_info(self, shop: Shop, date: str, cheque: dict) -> None:
        print(f"{self.name} rides to {shop.name}\n\n"
              f"Date: {date}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              "You have bought:")

        for product, price in cheque.items():
            if price % 1 == 0:
                price = int(price)
            print(f"{self.product_cart[product]} "
                  f"{product}s for {price} dollars")
