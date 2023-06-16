import json
from app.shop import Shop
from datetime import datetime


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.gas_prices = {
            "Outskirts Shop": 0,
            "Shop '24/7'": 0,
            "Central Shop": 0
        }
        self.cart_cost = {
            "Outskirts Shop": {
                "milk": 0,
                "bread": 0,
                "butter": 0
            },
            "Shop '24/7'": {
                "milk": 0,
                "bread": 0,
                "butter": 0
            },
            "Central Shop": {
                "milk": 0,
                "bread": 0,
                "butter": 0
            }
        }
        self.gas_cart = {
            "Outskirts Shop": 0, "Shop '24/7'": 0, "Central Shop": 0
        }
        self.money_after = 0
        self.best_price = 0
        self.best_shop = ""
        self.best_sum = 0


def customer_create_list() -> list[Customer]:
    customer_list = []

    with open(
            "/Users/anton/Projects/py-shop-trip/app/config.json"
    ) as f:
        config = json.load(f)
        for customer_attributes in config["customers"]:
            customer_obj = Customer(**customer_attributes)
            customer_list.append(customer_obj)

    return customer_list


def customer_calculations(
        list_of_customers: list[Customer],
        list_of_shops: list[Shop]
) -> None:

    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for cu in list_of_customers:
        for shop in list_of_shops:
            for key in (cu.product_cart.keys()):
                if shop.name == "Outskirts Shop":
                    cu.cart_cost["Outskirts Shop"][key] += round(
                        cu.product_cart[key] * shop.products[key], 2
                    )

                    cu.gas_cart[shop.name] = (
                        cu.gas_prices[shop.name]
                        + round(sum(cu.cart_cost[shop.name].values()), 2)
                    )

                if shop.name == "Shop '24/7'":
                    cu.cart_cost["Shop '24/7'"][key] += (
                        round(
                            cu.product_cart[key] * shop.products[key], 2
                        )
                    )
                    cu.gas_cart[shop.name] = (
                        cu.gas_prices[shop.name]
                        + round(sum(cu.cart_cost[shop.name].values()), 2)
                    )

                if shop.name == "Central Shop":
                    cu.cart_cost["Central Shop"][key] += (
                        round(
                            cu.product_cart[key] * shop.products[key], 2
                        )
                    )
                    cu.gas_cart[shop.name] = (
                        cu.gas_prices[shop.name]
                        + round(sum(cu.cart_cost[shop.name].values()), 2)
                    )

        cu.best_shop = min(
            cu.gas_cart, key=cu.gas_cart.get
        )

        cu.best_price = cu.gas_cart[cu.best_shop]
        cu.best_sum += sum(cu.cart_cost[cu.best_shop].values())

        if cu.best_price < cu.money:
            cu.money_after = cu.money - cu.best_price
            print(f"{cu.name} has {cu.money} dollars\n"
                  f"{cu.name}'s trip to the Outskirts Shop costs "
                  f"{cu.gas_cart['Outskirts Shop']}\n"
                  f"""{cu.name}'s trip to the Shop '24/7' costs """
                  f"""{cu.gas_cart["Shop '24/7'"]}\n"""
                  f"{cu.name}'s trip to the Central Shop costs "
                  f"{cu.gas_cart['Central Shop']}\n"
                  f"{cu.name} rides to {cu.best_shop}\n\n"

                  f"Date: {dt_string}\n"
                  f"Thanks, {cu.name}, for your purchase!\n"
                  f"You have bought:\n"
                  f"{cu.product_cart['milk']} milks for "
                  f"{cu.cart_cost[cu.best_shop]['milk']} dollars \n"
                  f"{cu.product_cart['bread']} breads for "
                  f"{cu.cart_cost[cu.best_shop]['bread']} dollars \n"
                  f"{cu.product_cart['butter']} butters for "
                  f"{cu.cart_cost[cu.best_shop]['butter']} dollars \n"
                  f"Total cost is {round(cu.best_sum, 2)} dollars\n"
                  f"See you again!\n\n"

                  f"{cu.name} rides home \n"
                  f"{cu.name} now "
                  f"has {round(cu.money_after, 2)} dollars \n"
                  )
        else:
            print(f"{cu.name} has {cu.money} dollars\n"
                  f"{cu.name}'s trip to the Outskirts Shop "
                  f"costs {cu.gas_cart['Outskirts Shop']}\n"
                  f"""{cu.name}'s trip to the Shop "24/7" """
                  f"""costs {cu.gas_cart["Shop '24/7'"]}\n"""
                  f"{cu.name}'s trip to the Central Shop "
                  f"costs {cu.gas_cart['Central Shop']}\n"
                  f"{cu.name} doesn't have "
                  f"enough money to make a purchase in any shop"
                  )
