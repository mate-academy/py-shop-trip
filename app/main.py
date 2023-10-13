from app.stores import stores
from app.customer import persons
import datetime


def date_time() -> str:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date


def shop_trip() -> str:
    cheapest_distance = 0
    cheapest_store = ""

    for person in persons:
        print(f"{person.name} has {person.money} dollars")

        for store in stores:
            total_cost = 0

            for key, value in person.product.items():
                if key in store.products:
                    unit_price = store.products[key]
                    product_cost = unit_price * value
                    total_cost += product_cost

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
            print(f"{person.name}'s trip to the {store.name} costs {distance}")

            if distance < cheapest_distance or cheapest_store == "":
                cheapest_distance = distance
                cheapest_store = store

        if person.money >= cheapest_distance:
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
