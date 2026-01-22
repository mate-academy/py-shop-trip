from __future__ import annotations
import math
import datetime

from app.models import Car, Customer, Shop


def add_models(config: dict) -> dict:
    data = {
        "customers": [],
        "shops": []
    }
    for customer in config["customers"]:
        data["customers"].append(
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
            )
        )
    for shop in config["shops"]:
        data["shops"].append(
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
        )
    return data


def calculate_distance(location1: list, location2: list) -> int | float:
    return math.sqrt(
        (location2[0] - location1[0])
        ** 2 + (location2[1] - location1[1]) ** 2
    )


def calculate_fuel_cost(
        distance: int | float,
        fuel_consumption: int | float,
        fuel_price: int | float
) -> int | float:
    return (fuel_consumption / 100) * distance * fuel_price


def create_check(customer: Customer, shops: dict) -> str:
    text = f"{customer.name} has {customer.money} dollars\n"

    for shop, money_and_check in shops.items():
        text += f"{customer.name}'s trip to the " \
                f"{shop} costs {money_and_check[0]}\n"
    min_cost_shop = min(shops, key=shops.get)

    if shops[min_cost_shop][0] > customer.money:
        text += f"{customer.name} doesn't have enough " \
                f"money to make a purchase in any shop"
        return text

    text += f"{customer.name} rides to {min_cost_shop}\n\n" \
            f"Date: " \
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n" \
            f"Thanks, {customer.name}, for your purchase!\n" \
            f"You have bought:\n" \
            f"{shops[min_cost_shop][1]}See you again!\n" \
            f"\n{customer.name} rides home\n" \
            f"{customer.name} now has " \
            f"{customer.money - shops[min_cost_shop][0]} dollars\n"
    return text
