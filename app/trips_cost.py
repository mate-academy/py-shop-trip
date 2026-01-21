from typing import List

from app.Car import Car
from app.customer import Customer


class Shop:
    shops = {}

    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops[self.name] = self


def calculate_trips_cost(
        customer: dict,
        shops: list,
        fuel_price: float
) -> tuple:
    car = Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
    customer = Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        car
    )
    print(f"{customer.name} has {customer.money} dollars")
    costs = {}
    shops_cost = {}
    for shop in shops:
        distance = ((((shop.location[0] - customer.location[0]) ** 2
                      + (shop.location[1] - customer.location[1]) ** 2)
                     ** 0.5) * 2)
        trip_cost = round(
            customer.car.fuel_consumption / 100 * distance * fuel_price,
            2)
        products_cost = {
            (product, amount): shop.products[product] * amount
            for product, amount in customer.product_cart.items()
        }
        cost = sum(products_cost.values()) + trip_cost
        costs[cost] = shop.name
        shops_cost[shop.name] = products_cost
        print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
    cheapest = min(costs)
    shop_name, min_price = costs[cheapest], shops_cost[costs[cheapest]]
    cheapest_shop = (shop_name, min_price)

    return cheapest, cheapest_shop, (customer.money - cheapest)
