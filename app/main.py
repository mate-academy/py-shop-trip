import datetime
import json
from app.customers import Customer, Car
from app.shops import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_cost = data.get("FUEL_PRICE")
    customers_list = []
    for customer in data.get("customers"):
        buyer = Customer(customer.get("name"),
                         customer.get("product_cart"),
                         customer.get("location"),
                         customer.get("money"),
                         Car(customer.get("car").get("brand"),
                             customer.get("car").get("fuel_consumption")))
        customers_list.append(buyer)
    shops_list = []
    for shop in data.get("shops"):
        mall = Shop(shop.get("name"),
                    shop.get("location"),
                    shop.get("products"))
        shops_list.append(mall)
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        minimum_cost = float("inf")
        for shop in shops_list:
            shop_cost = (customer.calculate_trip_cost(shop, fuel_cost)
                         + customer.shopping_cost(shop)["Total cost is "])
            if shop_cost < minimum_cost:
                minimum_cost = shop_cost
                cheapest_shop = shop
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {shop_cost}")
        if customer.money < minimum_cost:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        print(f"Date: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for item in customer.shopping_cost(cheapest_shop).items():
            print(f"{item[0]}{item[1]} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name}"
              f" now has {customer.money - minimum_cost} dollars\n")
