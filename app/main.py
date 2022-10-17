import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer.from_dict(person)
                 for person in data["customers"]]
    shops = [Shop.from_dict(shop)
             for shop in data["shops"]]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")
        choices = {}

        for shop in shops:
            if shop.is_in_stock(person.product_cart):
                receipt = shop.receipt(person.name,
                                       person.product_cart)
                choice = {"name": shop.name,
                          "receipt": receipt[1]}
                cost = receipt[0]
                cost += person.car.fuel_cost(person.location,
                                             shop.location,
                                             fuel_price)

                if person.money >= cost:
                    choices[cost] = choice
                print(f"{person.name}'s trip to the {shop.name} costs {cost}")

        if choices.keys():
            profit = min(choices.keys())
            person.money -= profit
            print(f'{person.name} rides to {choices[profit]["name"]}')
            print(choices[profit]["receipt"])
            print(f"{person.name} rides home")
            print(f"{person.name} now has {person.money} dollars\n")

        else:
            print(f"{person.name} doesn't have enough money "
                  f"to make purchase in any shop")
