import json
from app.costumer import Costumer
from app.shop import Shop
from app.trip_cost import trip_cost


def shop_trip() -> None:
    with open("app/config.json") as source:
        info = json.load(source)

    customers = [Costumer(customer) for customer in info["customers"]]
    shops = {market["name"]: Shop(market) for market in info["shops"]}

    for person in customers:
        result_trip = {}
        print(f"{person.name} has {person.money} dollars")

        for trip in shops:
            cost = trip_cost(info["FUEL_PRICE"], person, shops[trip])
            print(
                f"{person.name}'s trip"
                f" to the {trip} costs {cost}"
            )
            result_trip[cost] = trip

        if min(result_trip) > person.money:
            print(
                f"{person.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
        else:
            cheapest_shop = result_trip[min(result_trip)]
            print(f"{person.name} rides to {cheapest_shop}")
            print("\nDate: 04/01/2021 12:33:41")
            print(f"Thanks, {person.name}, for you purchase!")
            print("You have bought: ")
            products_price = 0

            for goods in person.product_cart:
                goods_price = (
                    person.product_cart[goods]
                    * shops[cheapest_shop].products[goods]
                )
                products_price += goods_price
                print(
                    f"{person.product_cart[goods]} {goods}s "
                    f"for {goods_price} dollars"
                )

            print(f"Total cost is {products_price} dollars")
            print("See you again!")
            print(f"\n{person.name} rides home")
            remaining_money = person.money - min(result_trip)
            print(f"{person.name} now has {round(remaining_money, 2)} dollars")
            print()


shop_trip()
