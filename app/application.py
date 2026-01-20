import json
from dataclasses import dataclass

from app.customer import Customer, convert_customer_from_dict
from app.shop import Shop, convert_shop_from_dict


@dataclass
class ShopTripApp:
    FUEL_PRICE: float
    customers: list[Customer]
    shops: list[Shop]

    def calculate_trip_cost(self, customer: Customer, shop: Shop) -> float:
        ride_cost = customer.calculate_cost_for_ride_to(
            shop.location, self.FUEL_PRICE
        )
        shop_cost = shop.calculate_cart_cost(customer.product_cart)
        trip_cost = round(ride_cost * 2 + shop_cost, 2)
        print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
        return trip_cost

    def process_the_data(self) -> None:
        for customer in self.customers:
            print(f"{customer.name} has {customer.rounded_money} dollars")
            trips_cost = list()
            for shop in self.shops:
                trips_cost.append(self.calculate_trip_cost(customer, shop))
            cheapest_trip_cost = min(trips_cost)
            if customer.money < cheapest_trip_cost:
                print(f"{customer.name} doesn't have enough money to make a "
                      "purchase in any shop")
                continue
            shop = self.shops[trips_cost.index(cheapest_trip_cost)]
            customer.ride_to_shop(shop.name, shop.location, self.FUEL_PRICE)
            check = shop.accept_client(customer)
            print(f"\n{check}\n")
            customer.ride_home(self.FUEL_PRICE)
            print(f"{customer.name} now has "
                  f"{customer.rounded_money} dollars\n")


def load_from_json(path: str) -> ShopTripApp:
    with open(path, "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = list(map(convert_customer_from_dict, data["customers"]))
    shops = list(map(convert_shop_from_dict, data["shops"]))
    return ShopTripApp(fuel_price, customers, shops)
