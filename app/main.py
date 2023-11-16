import json
import math
import operator

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as j_file:
        info = json.load(j_file)

    fuel_price = info["FUEL_PRICE"]

    customers = []
    for customer in info["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
        )

    shops = []
    for shop in info["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    all_customer_price = []
    for person in customers:
        each_customer_price = {}
        for shop_ in shops:
            distance = math.sqrt(
                (person.location[0] - shop_.location[0]) ** 2
                + (person.location[1] - shop_.location[1]) ** 2
            )
            location_cost = ((distance / 100)
                             * fuel_price
                             * person.car["fuel_consumption"])
            product_cost = sum(list(map(operator.mul,
                                        person.product_cart.values(),
                                        shop_.products.values())))
            each_customer_price.update(
                {shop_.name: round(location_cost * 2 + product_cost, 2)}
            )
        all_customer_price.append(each_customer_price)

    for i, d_ in enumerate(all_customer_price):
        name = customers[i].name
        f_shop = d_.get("Outskirts Shop")
        s_shop = d_.get("Shop '24/7'")
        t_shop = d_.get("Central Shop")
        print(f"{name} has {customers[i].money} dollars")
        print(f"{name}'s trip to the Outskirts Shop costs {f_shop}")
        print(f"{name}'s trip to the Shop '24/7' costs {s_shop}")
        print(f"{name}'s trip to the Central Shop costs {t_shop}")
        min_exp = min(d_.values())
        min_ind = list(d_.values()).index(min_exp)
        if min_exp > customers[i].money:
            print(f"{name} doesn't have enough money"
                  f" to make a purchase in any shop")
        else:
            shop_name = shops[min_ind].name
            print(f"{name} rides to {shop_name}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {name}, for your purchase!")
            print("You have bought:")
            milk = customers[i].product_cart["milk"]
            bread = customers[i].product_cart["bread"]
            butter = customers[i].product_cart["butter"]
            sh_milk = shops[min_ind].products["milk"]
            sh_bread = shops[min_ind].products["bread"]
            sh_butter = shops[min_ind].products["butter"]
            cost = milk * sh_milk + bread * sh_bread + butter * sh_butter
            print(f"{milk} milks for {milk * sh_milk} dollars")
            print(f"{bread} breads for {int(bread * sh_bread)} dollars")
            print(f"{butter} butters for {butter * sh_butter} dollars")
            print(f"Total cost is {cost} dollars")
            print("See you again!\n")
            print(f"{name} rides home")
            print(f"{name} now has "
                  f"{customers[i].money - all_customer_price[i][shop_name]} "
                  f"dollars\n")
