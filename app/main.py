import os
import json
import datetime
from app.shop import Shop, Customer


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as json_file:
        info = json.load(json_file)
        fuel_price = info["FUEL_PRICE"]
        customers = [
            Customer.deserialize_from_dict(customer)
            for customer in info["customers"]
        ]
        shops = [
            Shop.deserialize_from_dict(shop)
            for shop in info["shops"]
        ]
        for person in customers:
            print(f"{person.name} has {person.money} dollars")
            check = []
            for shop in shops:
                trip_cost = person.calculate_trip_cost(shop, fuel_price)
                products_cost = shop.get_total_cost(person)
                total = products_cost + trip_cost
                print(f"{person.name}'s trip to the {shop.name} costs {total}")
                if not check:
                    check.extend([total, products_cost, shop])
                else:
                    if total < check[0]:
                        check[0] = total
                        check[1] = products_cost
                        check[2] = shop
            if person.money >= check[0]:
                print(f"{person.name} rides to {check[2].name}" + "\n")
                date_string = datetime.datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )
                print(f"Date: {date_string}")
                print(f"Thanks, {person.name}, for your purchase!")
                print("You have bought: ")
                for order in person.orders:
                    item_cost = check[2].products.get(
                        order.product.name
                    ).price * order.amount
                    print(f"{order.amount} {order.product.name}s"
                          f" for {item_cost} dollars")
                print(f"Total cost is {check[1]} dollars")
                print("See you again!\n")
                print(f"{person.name} rides home")
                person.money -= check[0]
                print(f"{person.name} now has {person.money} dollars" + "\n")
            else:
                print(f"{person.name} doesn't have enough money "
                      f"to make a purchase in any shop")
