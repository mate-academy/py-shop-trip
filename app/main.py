import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("./app/config.json") as file:
        context = json.load(file)
    fuel_price = context["FUEL_PRICE"]
    customers = [
        Customer.load_from_dict(customer) for customer in context["customers"]
    ]
    shops = [
        Shop.load_from_dict(shop) for shop in context["shops"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        options = {}
        for shop in shops:
            money = round(
                customer.calculate_way_to_shop(shop, fuel_price) * 2
                + customer.calculate_products_cost(shop),
                2,
            )
            options[money] = shop
            print(f"{customer.name}'s trip to the {shop.name} costs {money}")
        selected_shop = options[min(options)]

        if options and min(options) <= customer.money:
            print(f"{customer.name} rides to {options[min(options)].name}")
            customer.create_chek(selected_shop)
            print(
                f"{customer.name} rides home\n{customer.name} now has "
                f"{round(customer.money - min(options), 2)} dollars\n"
            )

        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
