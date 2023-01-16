from __future__ import annotations
import datetime
from app.json_handling import SHOPS, FUEL_PRICE
from app.classes import Customer, Shop


def to_shop_distance(customer: Customer, shop: Shop) -> float:
    x1 = customer.location[0]
    y1 = customer.location[1]
    x2 = shop.location[0]
    y2 = shop.location[1]
    result = (((x2 - x1) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    return result


def cost_drive_to_shop(customer: Customer, shop: Shop) -> float:
    distance = to_shop_distance(customer, shop)
    one_km_consumption = customer.car.fuel_consumption / 100
    consumption_for_trip = distance * one_km_consumption
    final_cost = consumption_for_trip * FUEL_PRICE
    return final_cost


def charge_for_trip(func: callable) -> callable:
    def handler(customer: Customer, shop: Shop) -> callable:
        charge = float(cost_drive_to_shop(customer, shop))
        customer.money -= charge
        func(customer, shop)
        customer.money -= charge
    return handler


def choose_shop(customer: Customer, shops: SHOPS) -> Shop | None:
    comparison_dict = {}
    for shop in shops:
        if not check_shops_products(customer, shop):
            continue
        travel_cost = cost_drive_to_shop(customer, shop) * 2
        products_cost = sum(
            customer.products_to_buy[product] * shop.products_provides[product]
            for product in customer.products_to_buy.keys()
        )
        total_cost = round(travel_cost + products_cost, 2)
        comparison_dict[total_cost] = shop
        print(
            f"{customer.name}'s trip to the {shop.name} costs {total_cost}"
        )
    suitable_cost = min(comparison_dict)
    if customer.money < suitable_cost:
        print(f"{customer.name} doesn't have enough "
              f"money to make purchase in any shop")
    else:
        shop_to_ride = comparison_dict[suitable_cost]
        print(f"{customer.name} rides to {shop_to_ride.name}\n")
        return shop_to_ride


def check_shops_products(customer: Customer, shop: Shop) -> bool:
    for product in customer.products_to_buy:
        if product not in shop.products_provides:
            print(f"Shop {shop.name} doesn't provides {product}")
            return False
        return True


def date_greeting_farewell(func: callable) -> callable:
    def handler(customer: Customer, shop: Shop) -> callable:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer.name}, for you purchase!")
        func(customer, shop)
        print("See you again!\n")
    return handler


@charge_for_trip
@date_greeting_farewell
def sell_products(customer: Customer, shop: Shop) -> None:
    print("You have bought: ")
    total_cost = 0
    for product in customer.products_to_buy:
        quantity = customer.products_to_buy[product]
        price = shop.products_provides[product]
        charge = quantity * price
        total_cost += charge
        customer.money -= charge
        print(f"{quantity} {product}s for {charge} dollars")
    print(f"Total cost is {total_cost} dollars")
