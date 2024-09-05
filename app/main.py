import json
import datetime


from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as js:
        config = json.load(js)

    fuel_price = config["FUEL_PRICE"]

    list_of_shops = [Shop(shop["name"],
                          shop["location"],
                          shop["products"]) for shop in config["shops"]]

    list_of_customers = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 customer["car"]) for customer in config["customers"]]

    for person in list_of_customers:
        print(f"{person.name} has {person.money} dollars")

        lowest_cost = person.cash_flow(list_of_shops, fuel_price)
        shop = lowest_cost["shop"]

        if lowest_cost["cost"] <= person.money:
            print(f"{person.name} rides to {shop.name}")
            print(f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {person.name}, for your purchase!\n"
                  f"You have bought:")

            total_cost = 0

            for product in person.product_cart.keys():
                product_quantity = person.product_cart[product]
                cost_of_products = (shop.products[product]
                                    * person.product_cart[product])

                if isinstance(
                        cost_of_products,
                        float) and cost_of_products % 1 == 0:
                    cost_of_products = int(cost_of_products)

                print(f"{product_quantity} {product}s "
                      f"for {cost_of_products} dollars")
                total_cost += (shop.products[product]
                               * person.product_cart[product])
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")
            person.money -= lowest_cost["cost"]
            print(f"{person.name} rides home\n{person.name} n"
                  f"ow has {person.money} dollars\n")
        else:
            print(f"{person.name} doesn't have enough money to"
                  f" make a purchase in any shop")
