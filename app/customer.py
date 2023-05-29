import dataclasses
import json
import math
from app.shop import Shop

with open("config.json", "r") as file:
    data = json.load(file)


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict


fuel_price = data["FUEL_PRICE"]
customers_data = data['customers']


customers = [Customer(
    name=customer['name'],
    product_cart=customer['product_cart'],
    location=customer['location'],
    money=customer['money'],
    car=customer['car']
) for customer in customers_data]


def fuel_cost(customer: Customer, shop: [Shop]) -> float:
    fuel_consumption = customer.car["fuel_consumption"]
    cost_of_fuel = 0
    customer_location = customer.location
    shop_location = shop.location
    distance_to_shop = math.sqrt((shop_location[0] - customer_location[0])
                                 ** 2 + (shop_location[1] - shop_location[1]) ** 2)
    cost_of_fuel += 2 * distance_to_shop * (fuel_consumption / 100) * fuel_price
    return cost_of_fuel


def the_cost_of_shopping(customer: Customer, shop: Shop) -> float:
        cost = 0

        for product, quantity in customer.product_cart.items():
            if product in shop.products:
                price = shop.products[product]
                cost += price * quantity
                cost += fuel_cost(customer, shop)
                print(f"{customer.name}'s trip to {shop.name} costs {cost}")
        return cost


def cheapest_shop(customer: Customer, shops: list[Shop]) -> Shop:
    total_cost = float('inf')
    selected_shop = None

    for shop in shops:
        cost = the_cost_of_shopping(customer, shop)
        if cost < total_cost:
            total_cost = cost
            selected_shop = shop

    if selected_shop is None:
        raise ValueError(f"{customer.name} doesn't have enough money to make a purchase in any shop")
    customer.location = selected_shop.location

    return selected_shop


def calculate_total_cost(customer: Customer, shop: Shop) -> str:
    total_cost = 0
    output = "You have bought:\n"

    for product, quantity in customer.product_cart.items():
        if product in shop.products:
            price = shop.products[product]
            cost = price * quantity
            total_cost += cost
            output += f"{quantity} {product}s for {cost} dollars\n"

    output += f"Total cost is {total_cost} dollars\nSee you again!"
    return output
