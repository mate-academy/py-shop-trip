import datetime
import math
import dataclasses

from app.customer import Customer, convert_file
from app.shop import create_shops, Shop


@dataclasses.dataclass
class Roads:
    count_trip = None
    min_cost = float("inf")
    closest_shop = None
    list_of_count = []
    location_customer = None

    def car_count_trip(self, person: Customer,
                       market: Shop) -> int:
        coord_customer = person.location
        x1, y1 = coord_customer[0], coord_customer[1]

        coord_shop = market.location
        x2, y2 = coord_shop[0], coord_shop[1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 2
        distance_km = round(distance, 2)
        self.count_trip = round(((((person.car["fuel_consumption"] * (
            distance_km) / 100) * convert_file()["FUEL_PRICE"]))), 2)
        for key, value in person.product_cart.items():
            unit_price = market.products[key]
            product_cost = unit_price * value
            self.count_trip += product_cost
        return self.count_trip

    def find_chip_market(self, person: Customer) -> None:
        self.min_cost = float("inf")
        print(f"{person.name} has {person.money} dollars")
        for market in create_shops():
            cost_trip = self.car_count_trip(person, market)
            print(f"{person.name}'s trip to the {market.name} "
                  f"costs {round(cost_trip, 2)}")
            if cost_trip < self.min_cost:
                self.min_cost = cost_trip
                self.closest_shop = market
        if self.min_cost < person.money:
            print(f"{person.name} rides to {self.closest_shop.name}\n")
            self.location_customer = person.location
            person.location = self.closest_shop.location
        else:
            print(f"{person.name} doesn't have enough money"
                  f" to make a purchase in any shop")

    def count_customer_check(self, person: Customer) -> None:
        total_customer_cost = 0
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}\n"
              f"Thanks, {person.name}, for your purchase!\n"
              f"You have bought: ")

        for key, value in person.product_cart.items():
            unit_price = self.closest_shop.products[key] * value
            if isinstance(unit_price, float) and unit_price.is_integer():
                unit_price = int(unit_price)
            total_customer_cost += unit_price
            print(f"{person.product_cart[key]} {key}s "
                  f"for {unit_price} dollars")
        print(f"Total cost is {total_customer_cost} dollars")
        print("See you again!\n")

    def fuel_cost_get_at_home(self, person: Customer) -> None:

        print(f"{person.name} rides home")
        person.location = self.location_customer
        print(f"{person.name} now "
              f"has {round(person.money - self.min_cost, 2)} dollars\n")
