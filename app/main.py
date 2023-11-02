from app.customer import Customer
from app.shop import Shop
import json


def shop_trip() -> None:
    config_data = load_config_data()
    fuel_price = config_data["FUEL_PRICE"]
    customer_data = create_customers(config_data)
    shop_data = create_shops(config_data)

    for customer in customer_data:
        customer.primary_amount_of_money()
        shops_cost = calculate_trip_costs(customer, shop_data, fuel_price)
        min_shop = find_cheapest_shop(shops_cost)

        if min_shop and customer.money >= shops_cost[min_shop]:
            make_purchase_trip(customer, min_shop, shops_cost)
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


def load_config_data() -> dict:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
    return config_data


def create_customers(config_data: dict) -> list:
    customer_data = config_data["customers"]
    return [
        Customer(**customer)
        for customer in customer_data
    ]


def create_shops(config_data: dict) -> list:
    shop_data = config_data["shops"]
    return [Shop(**shop) for shop in shop_data]


def calculate_trip_costs(
        customer: Customer,
        shop_data: list,
        fuel_price: float
) -> dict:
    trip_costs = {}
    for shop in shop_data:
        products_cost = shop.calculate_purchase_cost(customer)
        fuel_cost = customer.car.calculate_fuel_cost(
            shop.calculate_distance_to_customer(customer), fuel_price
        )
        trip_cost = round(products_cost + fuel_cost * 2, 2)
        trip_costs[shop] = trip_cost
        print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
    return trip_costs


def find_cheapest_shop(trip_costs: dict) -> Shop:
    min_cost = float("inf")
    min_shop = None
    for shop, cost in trip_costs.items():
        if cost < min_cost:
            min_cost = cost
            min_shop = shop
    return min_shop


def make_purchase_trip(
        customer: Customer,
        shop: Shop,
        shops_cost: dict
) -> None:
    shop.print_rides_to_shop(customer)
    shop.print_receipt(customer)
    customer.print_rides_home()
    customer.money -= shops_cost[shop]
    customer.final_amount_of_money()
