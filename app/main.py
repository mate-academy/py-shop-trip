import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        file_json = json.load(config_file)

    fuel_price = file_json["FUEL_PRICE"]
    customers = file_json["customers"]
    shops = [Shop(shop) for shop in file_json["shops"]]

    for customer in customers:
        one_customer = Customer(customer)

        best_shop, best_price = one_customer.find_cheap_shop(fuel_price, shops)
        if best_price >= one_customer.money:
            print(f"{one_customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            break
        one_customer.left_money_after_shopping(
            best_shop, fuel_price, best_price
        )
        best_shop.purchase_receipt(one_customer.name,
                                   one_customer.product_cart)
        one_customer.way_home()
