import app.utilities as util
from app.classes.customer import Customer
from app.classes.car import Car
from app.classes.shop import Shop


def shop_trip():
    config = util.parse_json("app/config.json")

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer.from_dict(customer)
                 for customer in config["customers"]]
    shops = [Shop.from_dict(shop)
             for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        closest_shop = 0
        min_cost = 0
        for index, shop in enumerate(shops):
            trip_cost = 2 * util.calculate_trip_cost(fuel_price,
                                                     customer.car.fuel_consumption,
                                                     customer.location,
                                                     shop.location)

            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {trip_cost}")

            if trip_cost < min_cost:
                min_cost = trip_cost
                closest_shop = index

        if customer.money < min_cost:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {shops[closest_shop].name}\n")
        shopping_cost = shops[closest_shop].print_receipt(customer)

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - min_cost - shopping_cost}\n")
