import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as file:
        readfile = json.load(file)

    better_trip = 100000
    better_shop = ""
    for customer_dict, _ in enumerate(readfile["customers"]):
        customer = Customer(
            name=readfile["customers"][customer_dict]["name"],
            money=readfile["customers"][customer_dict]["money"],
            car=readfile["customers"][customer_dict]["car"],
            location=readfile["customers"][customer_dict]["location"],
            product_cart=readfile["customers"][customer_dict]["product_cart"]
        )

        customer.customers_money()
        for shop_dict, _ in enumerate(readfile["shops"]):
            car = Car(
                fuel_price=readfile["FUEL_PRICE"],
                fuel_consumption=readfile["customers"][customer_dict]
                ["car"]["fuel_consumption"]
            )
            shop = Shop(
                name=readfile["shops"][shop_dict]["name"],
                location=readfile["shops"][shop_dict]["location"],
                products=readfile["shops"][shop_dict]["products"])
            shop.customers_trip(customer.name,
                                shop.sum_of_products(customer.product_cart),
                                car.trip_to_shop(customer.location,
                                                 shop.location))
            if (
                    shop.sum_of_products(customer.product_cart)
                    + car.trip_to_shop(customer.location,
                                       shop.location)) < better_trip:
                better_trip = (
                    shop.sum_of_products(customer.product_cart)
                    + car.trip_to_shop(customer.location, shop.location)
                )
                better_shop = shop.name
        if better_trip < customer.money:
            print(f"{customer.name} rides to {better_shop}")
            print()
            for shop_dict, i in enumerate(readfile["shops"]):
                if i["name"] == better_shop:
                    shop = Shop(
                        name=readfile["shops"][shop_dict]["name"],
                        location=readfile["shops"][shop_dict]["location"],
                        products=readfile["shops"][shop_dict]["products"])
                    shop.buy_products(
                        customer.product_cart,
                        shop.sum_of_products(customer.product_cart),
                        customer.name
                    )
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {customer.money - better_trip} dollars")
            print()
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
