import json

from typing import Any, List, Dict

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_data() -> Dict[str, Any]:
    with open("app/config.json") as f:
        data = json.load(f)
        return data


def init_customers(data: Dict[str, Any]) -> List[Customer]:
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
        )
        for customer in data["customers"]
    ]
    return customers


def init_shops(data: Dict[str, Any]) -> List[Shop]:
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        for shop in data["shops"]
    ]
    return shops


def shop_trip() -> None:
    data = load_data()
    customers = init_customers(data)
    shops = init_shops(data)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        all_sum_trip = []
        for shop in shops:
            distance = customer.calculate_distance(shop.location)
            all_sum = (
                customer.calculate_trip_cost(distance, shop, data), shop.name
            )
            all_sum_trip.append(all_sum)
            customer.print_trip_summary(shop, all_sum)

        all_sum_trip = sorted(all_sum_trip)
        if customer.money > all_sum_trip[0][0]:
            chosen_shop = customer.choose_cheapest_shop(shops, all_sum_trip)
            customer.print_way_to_shop(chosen_shop)
            customer.show_receipt(chosen_shop)
            customer.print_way_to_home()
            customer.money -= all_sum_trip[0][0]
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
