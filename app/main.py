import datetime
import math
from app.shop import Shop
from app.customer import Person
from typing import Union


def date_time() -> str:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date


def calculate_distance(
    person: Person,
    shop: Shop
) -> Union[float, int]:
    total_cost = sum(
        shop.products[product_name] * product_want_to_buy
        for product_name, product_want_to_buy in person.product.items()
        if product_name in shop.products
    )
    distance_cost = person.car_fuel_consumption / 100
    distance = math.sqrt(
        (shop.location[0] - person.location[0]) ** 2
        + (shop.location[1] - person.location[1]) ** 2
    )
    all_distance = round(
        (distance * distance_cost * person.fuel_price * 2)
        + total_cost, 2
    )
    return all_distance


def shop_trip() -> str:
    cheapest_distance = float("inf")
    cheapest_shop = None
    persons = Person.people_load()
    shops = Shop.get_shop()
    for person in persons:
        print(f"{person.name} has {person.money} dollars")
        for shop in shops:
            distance = calculate_distance(person, shop)
            print(f"{person.name}'s trip to the {shop.name} costs {distance}")
            if distance < cheapest_distance:
                cheapest_distance = distance
                cheapest_shop = shop
        if person.money >= cheapest_distance:
            person.location = cheapest_shop.location
            print(
                f"{person.name} rides to {cheapest_shop.name}\n"
                f"\nDate: {date_time()}\n"
                f"Thanks, {person.name}, for your purchase!\n"
                "You have bought:"
            )
            all_products = 0
            for key, value in person.product.items():
                if key in cheapest_shop.products:
                    product_price = cheapest_shop.products[key]
                    count = product_price * value
                    all_products += count
                    total_price = str(product_price * value)
                    print(
                        f"{value} {key}s for "
                        f"{total_price.rstrip('0').rstrip('.')} dollars"
                    )

            print(f"Total cost is {all_products} dollars\n"
                  "See you again!")
            person.money -= cheapest_distance
            print(
                f"\n{person.name} rides home\n"
                f"{person.name} now has {person.money} "
                f"dollars\n"
            )
        else:
            print(
                f"{person.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
