import json
import math
from app.purchase import Purchase


with open("app/config.json", "r") as data_customers:
    data = json.load(data_customers)


class GetMostCheapShop(Purchase):
    def __init__(self, data_file: dict) -> None:
        super().__init__(data_file)

    def fuel_costs(self, shop: dict, customer: dict) -> None:
        fuel_price = self.data["FUEL_PRICE"]
        car_consumption = customer["car"]["fuel_consumption"]
        distance = math.dist(customer["location"], shop["location"])
        return round(distance * 2 / 100 * car_consumption * fuel_price, 2)

    def how_much_costs_trip(self, customers: dict) -> dict:
        customer_chart_milk = customers["product_cart"]["milk"]
        customer_chart_bread = customers["product_cart"]["bread"]
        customer_chart_butter = customers["product_cart"]["butter"]
        most_cheap_shop = {}

        for shop in data["shops"]:
            product = shop["products"]
            dollars_to_trip = (
                product["milk"] * customer_chart_milk
                + product["bread"] * customer_chart_bread
                + product["butter"] * customer_chart_butter
                + self.fuel_costs(shop, customers)
            )
            most_cheap_shop[shop["name"]] = dollars_to_trip
            print(
                f"{customers['name']}'s trip to the "
                f"{shop['name']} costs {most_cheap_shop[shop['name']]}"
            )
        return most_cheap_shop

    def choose_the_shop(self) -> None:
        for item in self.data["customers"]:
            name = item["name"]
            money = item["money"]
            print(f"{name} has {money} dollars")
            list_of_info = self.how_much_costs_trip(item)

            most_cheap_shop = sorted(list_of_info.items(),
                                     key=lambda x: x[1])[0]
            if int(money) >= most_cheap_shop[1]:
                print(f"{name} rides to "
                      f"{most_cheap_shop[0]}\n")
                self.create_purchase(most_cheap_shop[0], name)
                print(f"{name} now has {money - most_cheap_shop[1]} dollars\n")

            else:
                print(f"{name} doesn't have enough "
                      f"money to make purchase in any shop")


def shop_trip() -> None:
    shop_trip_data_parse = GetMostCheapShop(data)
    return shop_trip_data_parse.choose_the_shop()
