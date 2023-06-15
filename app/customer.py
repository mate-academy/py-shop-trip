import datetime

from app.extra import Car
from app.extra import Point
from app.shop import Shop


class Customer:

    @classmethod
    def from_dict(cls, customers_data: dict) -> list:
        return [cls(
                customer["name"],
                customer["product_cart"],
                Point(*customer["location"]),
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]),
                ) for customer in customers_data]

    def __init__(self,
                 name: str, product_cart: dict, location: Point,
                 money: int | float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def print_header(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_trip_cost(self, shop: Shop, fuel_price: float) -> dict:
        shop_billing = shop.calculate_cart(self.product_cart)
        shop_total = shop_billing.get("total")
        dist_fuel_total = (Point.calc_dist(self.location, shop.location)
                           * self.car.fuel_consumption)
        cost_of_trip = (shop_total
                        + round(0.02 * dist_fuel_total * fuel_price, 2))
        print(f"{self.name}'s trip to "
              f"the {shop.name} costs {str(cost_of_trip)}")
        trip_billing = shop_billing
        trip_billing["total"] = cost_of_trip
        return trip_billing

    def check_money_for_trip(self, trip_billing: dict) -> None:
        cheapest_shop = trip_billing.get("shop")
        if self.money >= trip_billing.get("total"):
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            home_point, self.location = self.location, cheapest_shop.location
            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {now}")
            print(f"Thanks, {self.name}, for your purchase!\n"
                  f"{trip_billing.get('check')}")
            print(f"{self.name} rides home")
            self.location = home_point
            self.money -= trip_billing.get("total")
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} doesn't have "
                  f"enough money to make a purchase in any shop")
