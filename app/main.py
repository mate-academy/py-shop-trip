from json import load

from app.car import Car, GasStation
from app.customer import Customer
from app.shop import Shop

FILE_NAME = "app/config.json"


def create_instance_customers(story: dict):
    customers = [
        Customer(
            name=customer["name"],
            products_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"])
        )
        for customer in story["customers"]
    ]
    return customers


def create_instance_shops(story: dict):
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in story["shops"]
    ]
    return shops


def shop_trip():
    with open(FILE_NAME, "r") as config_file:
        story = load(config_file)
    gas_station = GasStation(story["FUEL_PRICE"])
    customers = create_instance_customers(story)
    shops = create_instance_shops(story)

    for person in customers:

        print(f"{person.name} has {person.money} dollars")

        totals_costs_for_each_shop = {}
        for shop in shops:
            cost_trip = person.total_cost_trip(shop, gas_station)
            totals_costs_for_each_shop[shop] = cost_trip
            print(f"{person.name}'s trip to the {shop.name} costs {cost_trip}")

        min_cost = min(list(totals_costs_for_each_shop.values()))
        visit_shop = False

        for shop, cost_for_go_to_shop in totals_costs_for_each_shop.items():
            if cost_for_go_to_shop == min_cost and \
                    person.money >= person.total_cost_trip(shop, gas_station):
                person.go_to_shop(shop)
                person.change_location(shop.location)

                person.to_buy(min_cost)
                shop.print_purchase(person)
                visit_shop = True
                break

        if visit_shop:
            print(f"{person.name} rides home")
            person.check_money()
        else:
            print(f"{person.name} doesn't have enough money"
                  f" to make purchase in any shop")


if __name__ == '__main__':
    shop_trip()
