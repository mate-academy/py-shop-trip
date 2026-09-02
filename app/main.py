from app.customer import Customer
from app.shop import Shop
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        dict_if_info = json.load(file)

    dict_of_customers = dict_if_info["customers"]
    dict_of_shops = dict_if_info["shops"]

    price_of_fuel = dict_if_info["FUEL_PRICE"]

    list_of_customers = []
    list_of_shops = []

    for customer in dict_of_customers:
        list_of_customers.append(Customer(customer, price_of_fuel))

    for shop in dict_of_shops:
        list_of_shops.append(Shop(shop))

    for customer in list_of_customers:
        res = customer.how_much_money()
        print(res)
        for shop in list_of_shops:
            result = customer.full_price_of_trip(shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {result}")

        res = customer.cheapest_shop(list_of_shops)
        check = customer.have_money_for_product()
        if check is False:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(res)
        print()
        customer.cheapest_shop_for_customer.print_receipt(customer)
        print()
        print(f"{customer.name} rides home")
        money_left = customer.how_money_have_after_shopping(
            customer.cheapest_shop_for_customer
        )
        print(f"{customer.name} now has {money_left} dollars\n")
