import json
from app.customer import unpack_customers
from app.shop import unpack_shops


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = unpack_customers(data["customers"])
    shops = unpack_shops(data["shops"])
    ride_price_to_shop_list = []
    choose_shop = []

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            ride_price = customer.car.trip_price(fuel_price, customer.distance(shop.location))
            shop_price = 0
            for k, v in customer.product_cart.items():
                shop_price += v * shop.products[k]
            ride_price_to_shop_list.append(ride_price)
            total_price = ride_price + shop_price
            choose_shop.append(total_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {total_price}")
        shop_to_ride = shops[choose_shop.index(min(choose_shop))]
        if customer.money > min(choose_shop):

            print(f"{customer.name} rides to {shop_to_ride.name}\n")
        else:
            print(f"{customer.name} doesn't have enough money to make purchase in any shop")
            ride_price_to_shop_list.clear()
            choose_shop.clear()
            break
        shop_to_ride.recipe(customer)

        customer.car.ride_home(customer)
        print(f"{customer.name} now has {round((customer.money - min(choose_shop)), 2)} dollars\n")

        ride_price_to_shop_list.clear()
        choose_shop.clear()

