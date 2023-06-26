from dataclasses import dataclass
from app.customer import Customer
from app.car import Car
import math


@dataclass
class Shop:
    name: str
    location: list
    products: dict


def calculate_distance(client: Customer, shop: Shop) -> float:
    return math.sqrt(
        ((client.location[0] - shop.location[0]) ** 2)
        + ((client.location[1] - shop.location[1]) ** 2))


def calculate_trip_price(
        fuel_price: float,
        client: Customer,
        shops: dict,
        car: Car
) -> dict:
    trip_prices = {}
    for shop in shops.values():
        trip_price = (fuel_price * calculate_distance(client, shop)
                      * (car.fuel_consumption / 100) * 2)
        for product, price in shop.products.items():
            if product in client.products_cart:
                trip_price += (price * client.products_cart.get(product))
        trip_price = round(trip_price, 2)
        print(f"{client.name}'s trip to the {shop.name} costs {trip_price}")
        trip_prices[shop.name] = trip_price
    return trip_prices


def check_best_price(
        trip_prices: dict,
        client: Customer,
        shops: dict
) -> None:
    best_choice = min(trip_prices.values())
    best_shop = min(trip_prices, key=trip_prices.get)
    rest = client.money - best_choice
    if best_choice > client.money:
        print(
            f"{client.name} doesn't have enough money "
            f"to make a purchase in any shop")
    else:
        print(f"{client.name} rides to {best_shop}\n")
        create_bill(client, shops, best_shop)
        print(f"{client.name} rides home\n"
              f"{client.name} now has {rest} dollars\n")


def create_bill(client: Customer, shops: dict, best_shop: str) -> None:
    shop_price = 0
    print("Date: 04/01/2021 12:33:41")
    print(f"Thanks, {client.name}, for your purchase!\n"
          f"You have bought: ")
    for product in client.products_cart:
        product_price = (shops[best_shop].products[product]
                         * client.products_cart[product])
        shop_price += product_price
        print(f"{client.products_cart[product]} "
              f"{product}s for {product_price} dollars")
    print(f"Total cost is {shop_price} dollars\n"
          f"See you again!\n")
