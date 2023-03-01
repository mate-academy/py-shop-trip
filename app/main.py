import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = [Shop(one_shop) for one_shop in data["shops"]]
    for customer_dict in customers:
        customer = Customer(customer_dict)
        best_shop, overall_cost = customer.plan_shopping(shops, fuel_price)
        if customer.money <= overall_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
            break
        customer.go_shopping(best_shop, fuel_price, overall_cost)
        best_shop.print_receipt(customer.name, customer.product_cart)
        customer.back_home()


# my_data = {
#     "FUEL_PRICE": 2.4,
#     "customers": [
#         {
#             "name": "Bob",
#             "product_cart": {
#                 "milk": 4,
#                 "bread": 2,
#                 "butter": 5
#             },
#             "location": [12, -2],
#             "money": 55,
#             "car": {
#                 "brand": "Suzuki",
#                 "fuel_consumption": 9.9
#             }
#         },
#         {
#             "name": "Alex",
#             "product_cart": {
#                 "milk": 2,
#                 "bread": 2,
#                 "butter": 2
#             },
#             "location": [1, -2],
#             "money": 41,
#             "car": {
#                 "brand": "BMW",
#                 "fuel_consumption": 9.1
#             }
#         },
#         {
#             "name": "Monica",
#             "product_cart": {
#                 "milk": 3,
#                 "bread": 3,
#                 "butter": 1
#             },
#             "location": [11, -2],
#             "money": 12,
#             "car": {
#                 "brand": "Audi",
#                 "fuel_consumption": 7.6
#             }
#         }
#     ],
#     "shops": [
#         {
#             "name": "Outskirts Shop",
#             "location": [10, -5],
#             "products": {
#                 "milk": 3,
#                 "bread": 1,
#                 "butter": 2.5
#             }
#         },
#         {
#             "name": "Shop '24/7'",
#             "location": [4, 3],
#             "products": {
#                 "milk": 2,
#                 "bread": 1.5,
#                 "butter": 3.2
#             }
#         },
#         {
#             "name": "Central Shop",
#             "location": [0, 0],
#             "products": {
#                 "milk": 3,
#                 "bread": 2,
#                 "butter": 3.5
#             }
#         }
#     ]
# }
#
# shop_trip(my_data)
