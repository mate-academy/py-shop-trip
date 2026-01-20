import json
from app.shop import Shop
from app.car import Car
from app.customer import Customer
import datetime
from typing import Optional


def visit_shop_func(self: Customer, shop: Shop) -> None:
    now = datetime.datetime.now()
    print(
        f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"Thanks, {self.name}, for your purchase!\n"
        "You have bought:")
    total_cost = 0
    for product in shop.products:
        price_product = self.product_list[product] * shop.products[product]
        total_cost += price_product
        if int(price_product) == price_product:
            price_product = int(price_product)
        print(f"{self.product_list[product]} {product}s"
              f" for {price_product} dollars")
    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")
    print(f"{self.name} rides home")
    print(f"{self.name} now has {self.money} dollars\n")


def make_a_trip(self: Customer, fuel_price: int,
                shops: list[Shop]) -> Optional[Shop]:
    print(f"{self.name} has {self.money} dollars")
    visit_shop_bool = False
    visit_shop = shops[0]
    expenses = self.money_to_reach_shop(shops[0], fuel_price)
    expenses += self.make_purchase(shops[0])
    if expenses <= self.money:
        visit_shop_bool = True
        visit_shop = shops[0]
    for shop in shops:
        new_expenses = self.money_to_reach_shop(shop, fuel_price)
        new_expenses += self.make_purchase(shop)
        print(f"{self.name}'s trip to the {shop.name} costs {new_expenses}")
        if new_expenses < expenses:
            expenses = new_expenses
            if expenses < self.money:
                visit_shop_bool = True
                visit_shop = shop
    if visit_shop_bool:
        print(f"{self.name} rides to {visit_shop.name}\n")
        self.money = round(self.money - expenses, 2)
        visit_shop_func(self, visit_shop)
    else:
        print(f"{self.name} doesn't have enough money "
              "to make a purchase in any shop")


def shop_trip() -> None:
    # write your code here
    with open("app/config.json", "r") as json_file:
        data = json.load(json_file)
        fuel_price = data["FUEL_PRICE"]
        customer_list = data["customers"]
        shop_list = data["shops"]

        customer_obj_list = [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(**customer["car"]),
            )
            for customer in customer_list
        ]
        shop_obj_list = [Shop(**shop) for shop in shop_list]
        for customer in customer_obj_list:
            shop = make_a_trip(customer, fuel_price, shop_obj_list)
            if shop:
                customer.make_purchase(shop)
