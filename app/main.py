import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as file:
        json_data = json.load(file)

    better_trip = 100000
    better_shop = ""
    for customer_dict in json_data["customers"]:
        customer = Customer(
            name=customer_dict["name"],
            money=customer_dict["money"],
            car=customer_dict["car"],
            location=customer_dict["location"],
            product_cart=customer_dict["product_cart"]
        )

        customer.customers_money()
        for shop_dict in json_data["shops"]:
            car = Car(
                fuel_price=json_data["FUEL_PRICE"],
                fuel_consumption=customer_dict["car"]["fuel_consumption"]
            )
            shop = Shop(
                name=shop_dict["name"],
                location=shop_dict["location"],
                products=shop_dict["products"])
            shop.customers_trip(customer.name,
                                shop.sum_of_products(customer.product_cart),
                                car.trip_to_shop(customer.location,
                                                 shop.location))
            trip_total_cost = (
                shop.sum_of_products(customer.product_cart)
                + car.trip_to_shop(customer.location, shop.location)
            )
            if trip_total_cost < better_trip:
                better_trip = trip_total_cost
                better_shop = shop.name
        if better_trip < customer.money:
            print(f"{customer.name} rides to {better_shop}")
            print()
            for shop_dict in json_data["shops"]:
                if shop_dict["name"] == better_shop:
                    shop = Shop(
                        name=shop_dict["name"],
                        location=shop_dict["location"],
                        products=shop_dict["products"])
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
