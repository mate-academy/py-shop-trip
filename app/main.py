import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        customers_json = json.load(config)

    customers = {}
    cars = {}
    for customer in customers_json["customers"]:
        customers.update({customer["name"]:
                          Customer(customer["name"],
                                   customer["product_cart"],
                                   customer["location"],
                                   customer["money"],
                                   customer["car"])
                          })
        cars.update({customer["name"]:
                     Car(customer["name"],
                         customers_json["FUEL_PRICE"],
                         customer["car"]["brand"],
                         customer["car"]["fuel_consumption"],
                         customer["location"])
                     })
    shops = {}
    for shop in customers_json["shops"]:
        shops.update({shop["name"]: Shop(shop["name"],
                                         shop["location"],
                                         shop["products"])
                      })

    for key_customer in customers:
        print(f"{key_customer} has {customers[key_customer].money} dollars")
        cost_shop = {}
        for key_shop in shops:
            cost_shop.update(
                {shops[key_shop].name:
                 shops[key_shop].products_cost_customer
                 (customers[key_customer])
                 + cars[key_customer].distance_two_way_cost
                 (shops[key_shop].location)})
            print(f"{key_customer}'s trip to the {key_shop} "
                  f"costs {cost_shop[shops[key_shop].name]}")
        shop_for_visit = min(cost_shop, key=cost_shop.get)
        if cost_shop[shop_for_visit] <= customers[key_customer].money:
            print(f"{key_customer} rides to {shop_for_visit}" + "\n")
            (cars[key_customer].change_car_location
             (shops[shop_for_visit].location))

            (customers[key_customer].change_customer_location
             (shops[shop_for_visit].location))

            shops[shop_for_visit].shopping_process(customers[key_customer])
            print(f"{key_customer} rides home")

            (cars[key_customer].change_car_location
             (cars[key_customer].location))

            (customers[key_customer].change_customer_location
             (cars[key_customer].location))

            customers[key_customer].money -= cost_shop[shop_for_visit]
            print(f"{key_customer} now has "
                  f"{customers[key_customer].money} dollars" + "\n")
        else:
            print(f"{key_customer} doesn't have enough money "
                  f"to make a purchase in any shop")
