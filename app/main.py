import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = [Shop(one_shop) for one_shop in data["shops"]]
    for customer_dict in customers:
        customer = Customer(customer_dict)
        best_shop, overall_cost = customer.plan_shopping(shops, fuel_price)
        if customer.money <= overall_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            break
        customer.go_shopping(best_shop, fuel_price, overall_cost)
        best_shop.print_receipt(customer.name, customer.product_cart)
        customer.back_home()
