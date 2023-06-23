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
            "Outskirts Shop": {},
            "Shop '24/7'": {},
            "Central Shop": {}
        }

        for key in self.product_cart.keys():
            self.cart_cost["Outskirts Shop"][key] = 0
            self.cart_cost["Shop '24/7'"][key] = 0
            self.cart_cost["Central Shop"][key] = 0

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
            "app/config.json"
    ) as f:
        config = json.load(f)
        for customer_attributes in config["customers"]:
            customer_obj = Customer(**customer_attributes)
            customer_list.append(customer_obj)

    return customer_list


def customer_calculations(
        customers: list[Customer],
        shops: list[Shop]
) -> None:
    for customer in customers:
        for shop in shops:
            for key in (customer.product_cart.keys()):
                customer.cart_cost[shop.name][key] += round(
                    customer.product_cart[key] * shop.products[key], 2
                )

                customer.gas_cart[shop.name] = (
                    customer.gas_prices[shop.name]
                    + round(sum(customer.cart_cost[shop.name].values()), 2)
                )

        customer.best_shop = min(
            customer.gas_cart, key=customer.gas_cart.get
        )

        customer.best_price = customer.gas_cart[customer.best_shop]
        customer.best_sum += sum(
            customer.cart_cost[customer.best_shop].values()
        )


def receipts(customer_list: list[Customer], shop_list: list[Shop]) -> None:
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for cstmr in customer_list:
        if cstmr.best_price < cstmr.money:
            cstmr.money_after = cstmr.money - cstmr.best_price
            print(f"{cstmr.name} has {cstmr.money} dollars")
            for shop in shop_list:
                print(f"{cstmr.name}'s trip to the {shop.name} costs "
                      f"{cstmr.gas_cart[shop.name]}")
            print(f"{cstmr.name} rides to {cstmr.best_shop}\n")

            print(f"Date: {dt_string}\n"
                  f"Thanks, {cstmr.name}, for your purchase!\n"
                  f"You have bought:")
            for product in cstmr.product_cart:
                print(f"{cstmr.product_cart[product]} {product}s for "
                      f"{cstmr.cart_cost[cstmr.best_shop][product]} dollars")
            print(
                f"Total cost is {round(cstmr.best_sum, 2)} dollars\n"
                f"See you again!\n\n"

                f"{cstmr.name} rides home \n"
                f"{cstmr.name} now "
                f"has {round(cstmr.money_after, 2)} dollars\n"
            )

        else:
            print(f"{cstmr.name} has {cstmr.money} dollars")
            for shop in shop_list:
                print(f"{cstmr.name}'s trip to the {shop.name} costs "
                      f"{cstmr.gas_cart[shop.name]}")
            print(f"{cstmr.name} doesn't have "
                  f"enough money to make a purchase in any shop"
                  )
