from app.stores import Store
from app.customer import Person
import datetime
from typing import Union, List


def date_time() -> str:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date


def calculate_distance(
        person: List[tuple],
        store: List[tuple]
) -> Union[float, int]:
    total_cost = sum(
        store.products[product_name] * product_price
        for product_name, product_price in person.product.items()
        if product_name in store.products
    )

    distance_cost = person.fuel_price * (person.fuel_consumption / 100)
    distance = round(
        (
            (
                (store.location[0] - person.location[0]) ** 2
                + (store.location[1] - person.location[1]) ** 2
            )
        )
        ** 0.5
        * 2
        * distance_cost
        + total_cost,
        2,
    )
    return distance


def shop_trip() -> str:
    cheapest_distance = 0
    cheapest_store = None
    persons = Person.load_people()
    stores = Store.get_stores()

    for person in persons:
        print(f"{person.name} has {person.money} dollars")

        for store in stores:
            distance = calculate_distance(person, store)

            print(f"{person.name}'s trip to the {store.name} costs {distance}")

            if distance < cheapest_distance or cheapest_store is None:
                cheapest_distance = distance
                cheapest_store = store

        if person.money >= cheapest_distance:
            person.location = cheapest_store.location
            print(
                f"{person.name} rides to {cheapest_store.name}\n"
                f"\nDate: {date_time()}\n"
                f"Thanks, {person.name}, for your purchase!\n"
                "You have bought: "
            )
            all_product = 0
            for key, value in person.product.items():
                if key in cheapest_store.products:
                    product_price = cheapest_store.products[key]
                    count = product_price * value
                    all_product += count
                    total_price = str(product_price * value)
                    print(
                        f"{value} {key}s for"
                        f" {total_price.rstrip('0').rstrip('.')}"
                        f" dollars"
                    )
            print(f"Total cost is {all_product} dollars\n" "See you again!")

            person.money -= cheapest_distance

            print(
                f"\n{person.name} rides home\n"
                f"{person.name} now has {person.money} dollars\n"
            )
        else:
            print(
                f"{person.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
