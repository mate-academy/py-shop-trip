import json
from shop import Shop
from customer import Customer


def shop_trip() -> None:

    with open("config.json", "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]

    customers = []

    for person in config_data["customers"]:
        customers.append(Customer(person["name"],
                                  person["product_cart"],
                                  person["location"],
                                  person["money"],
                                  person["car"]))

    shops = []

    for shop in config_data["shops"]:
        shops.append(Shop(shop["name"],
                          shop["location"],
                          shop["products"]))

    for person in customers:
        print(f"{person.name} has {person.money} dollars")
        ride_price = {}
        for place in shops:
            distance = 2 * person.distance(person.location, place.location)
            total_price = person.trip_cost(distance,
                                           fuel_price,
                                           place.products)
            if total_price <= person.money:
                ride_price[place.name] = total_price
            print(f"{person.name}'s trip to the {place.name} "
                  f"costs {round(total_price, 2)}")
        if len(ride_price) != 0:
            shop_price_tuple = [(key, value)
                                for key, value in ride_price.items()]
            sorted_price_tuple = sorted(shop_price_tuple, key=lambda x: x[1])
            sorted_price_dict = {key: value
                                 for key, value in sorted_price_tuple}
            shop_to_ride = next(iter(sorted_price_dict))
            print(f"{person.name} rides to {shop_to_ride}\n")
            for shop in shops:
                if shop.name == shop_to_ride:
                    shop.purchase(person.name, person.product_cart)
                    person.money -= sorted_price_dict[shop_to_ride]
            print(f"{person.name} rides home\n"
                  f"{person.name} now has {round(person.money, 2)} dollars\n")
        if len(ride_price) == 0:
            print(f"{person.name} doesn't have enough money "
                  f"to make purchase in any shop\n")


shop_trip()
