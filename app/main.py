import json
from app.shop import Shop
from app.car import Car
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
        fuel_price = config_data["FUEL_PRICE"]
        customers = config_data["customers"]
        shops = config_data["shops"]

    for customer in customers:
        Customer.load_from_dict(customer)

        client_car = Car(
            fuel_price,
            Customer.car["fuel_consumption"],
            Customer.location,
        )

        shops_calculate_with_trip = {}
        shops_calculate = {}
        print(f"{Customer.name} has {Customer.money} dollars")
        for shop_data in shops:
            shop = Shop(
                shop_data["name"],
                shop_data["location"],
                shop_data["products"],
            )
            shops_calculate[shop.shop_name] \
                = shop.calculate_product(Customer.product_cart)

            trip_cost = shop.sum_of_products(shops_calculate[shop.shop_name]) \
                + client_car.calculate_trip(shop.location_shop)

            shops_calculate_with_trip[shop.shop_name] = round(trip_cost, 2)

            print(f"{Customer.name}'s trip to the "
                  f"{shop.shop_name} costs {round(trip_cost, 2)}")

        cheapest_shop_name = \
            Customer.the_cheapest_trip_to_the_store(shops_calculate_with_trip)

        if shops_calculate_with_trip[cheapest_shop_name] > Customer.money:
            print(f"{Customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            continue
        print(f"{Customer.name} rides to {cheapest_shop_name}\n")

        shop_result = shops_calculate[cheapest_shop_name]
        Customer.print_check(
            Customer,
            shop_result,
            Shop.sum_of_products(shop_result),
        )
        spend_money = shops_calculate_with_trip[cheapest_shop_name]
        print(f"{Customer.name} rides home")
        print(f"{Customer.name} now has "
              f"{Customer.money - spend_money} dollars\n")
