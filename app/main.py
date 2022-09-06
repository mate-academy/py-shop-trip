import json
from app.customer import Customer
from app.shop import Shop
import datetime


def shop_trip():
    with open('app/config.json') as f:
        file = json.load(f)
    data_customers = file["customers"]
    data_shops = file["shops"]
    petrol = file["FUEL_PRICE"]

    for customer_ in data_customers:
        custom = Customer(customer_["name"],
                          customer_["product_cart"],
                          customer_["location"],
                          customer_["money"],
                          customer_["car"])

        custom.have_money()
        cost_shops = {}
        for shop_ in data_shops:

            shop = Shop(shop_["name"],
                        shop_["location"],
                        shop_["products"])
            a = shop.full_amount_shopping(custom, petrol)

            cost_shops[shop_["name"]] = a

            print(f"{customer_['name']}'s trip"
                  f" to the {shop_['name']} costs {str(a)}")

        if min(cost_shops.values()) <= customer_["money"]:
            item_ = ["", min(cost_shops.values())]
            for key, value in cost_shops.items():
                if value <= item_[1]:
                    item_ = [key, value]

            print(f"{customer_['name']} rides to {item_[0]}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer_['name']}, for you purchase!")
            print("You have bought: ")
            for shop_ in data_shops:

                if shop_["name"] == item_[0]:
                    shop = Shop(shop_["name"],
                                shop_["location"],
                                shop_["products"])

                    shop.bill_shop(custom)
                    full_shopping = \
                        shop.full_amount_shopping(custom, petrol)
                    count = custom.remainder_money(full_shopping)
                    cost_ = shop.total_cost(custom)
                    print(f"Total cost is {cost_} dollars")
                    print("See you again!\n")

                    print(f"{customer_['name']} rides home")
                    print(f"{customer_['name']} now"
                          f" has {count} dollars\n")
        else:
            print(f"{customer_['name']} doesn't have"
                  f" enough money to make purchase in any shop")
