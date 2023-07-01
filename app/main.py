import datetime
import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    for shop in config["shops"]:
        create_shop(shop)
    for node in config["customers"]:
        customer = create_customers(node)
        count_trip_costs_and_choose_shop(
            customer,
            Shop.shop_list,
            config["FUEL_PRICE"]
        )


def create_customers(customer: dict) -> Customer:
    return Customer(
        customer.get("name"),
        customer.get("product_cart"),
        customer.get("location"),
        customer.get("money"),
        Car(
            customer["car"].get("brand"),
            customer["car"].get("fuel_consumption")
        )
    )


def create_shop(shop: dict) -> Shop:
    return Shop(
        shop.get("name"),
        shop.get("location"),
        shop.get("products")
    )


def count_both_way_distance(
        customer: Customer,
        shop: Shop
) -> float:
    return round((((shop.location[0] - customer.location[0]) ** 2
                   + (shop.location[1] - customer.location[1])
                   ** 2) ** 0.5) * 2, 2)


def count_price_for_both_ways(
        customer: Customer,
        shop: Shop,
        price_per_liter: float
) -> float:
    distance = count_both_way_distance(customer, shop)
    return round((customer.car.fuel_consumption * distance / 100)
                 * price_per_liter, 2)


def count_price_for_all_products(
        customer: Customer,
        shop: Shop,
) -> float:
    return sum(
        [
            customer.products.get("milk") * shop.products.get("milk"),
            customer.products.get("bread") * shop.products.get("bread"),
            customer.products.get("butter") * shop.products.get("butter"),
        ]
    )


def count_trip_costs_and_choose_shop(
        customer: Customer,
        shops: list[Shop],
        price_per_liter: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    prices_of_trips = {}

    for shop in shops:
        price = (count_price_for_all_products(customer, shop)
                 + count_price_for_both_ways(customer, shop, price_per_liter))
        prices_of_trips[price] = shop
        print(f"{customer.name}'s trip to the {shop.name} costs {price}")

    if customer.money >= min(prices_of_trips.keys()):
        cheapest_shop = prices_of_trips[min(prices_of_trips.keys())]
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        price_for_trip = min(prices_of_trips.keys())
        print_recipe(customer, cheapest_shop, price_for_trip)
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")


def print_recipe(
        customer: Customer,
        shop: Shop,
        price_for_trip: float
) -> None:
    sum_total = 0
    print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
          f"Thanks, {customer.name}, for your purchase!\n"
          f"You have bought: ")

    for key, value in customer.products.items():
        price = value * shop.products.get(key)
        sum_total += price
        print(f"{value} {key}s for {price} dollars")

    print(f"Total cost is {sum_total} dollars\n"
          f"See you again!\n\n"
          f"{customer.name} rides home\n"
          f"{customer.name} now has "
          f"{customer.money - price_for_trip} dollars\n")
