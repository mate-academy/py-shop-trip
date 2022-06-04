import json
from app.classes.Customer import Customer
from app.classes.Shop import Shop
from app.classes.Car import Car


def shop_trip():
    with open("../app/config.json", "r") as f:
        file = json.load(f)

    customers = []
    shops = []
    for customer in file["customers"]:
        customers.append(Customer(customer["name"],
                                  customer["product_cart"],
                                  customer["location"],
                                  customer["money"],
                                  Car(customer["car"]["brand"],
                                      customer["car"]["fuel_consumption"]
                                      )
                                  )
                         )

    for shop in file["shops"]:
        shops.append(Shop(shop["name"],
                          shop["location"],
                          shop["products"]
                          )
                     )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.print_all_store_costs(shops)
        if customer.trip_cost(customer.cheapest_way(shops)) > customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            customer.go_to_shop(customer.cheapest_way(shops))
            customer.make_shopping(customer.cheapest_way(shops))
            customer.go_to_home(customer.cheapest_way(shops))
