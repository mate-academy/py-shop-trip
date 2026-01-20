from app.customer import Customer
from app.shop import Shop
from app.car import Car
from app.config import config


def shop_trip() -> None:
    customers = []
    for customer in config["customers"]:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        customers.append(Customer(customer["name"],
                                  customer["product_cart"],
                                  customer["location"],
                                  customer["money"], car))

    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        for shop in shops:
            trip_costs[shop.name] = customer.calculate_trip_cost(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_costs[shop.name]:.2f}")
        cheapest_shop = min(trip_costs, key=trip_costs.get)
        if customer.money >= trip_costs[cheapest_shop]:
            customer.ride_to_shop(next(shop
                                       for shop in shops
                                       if shop.name == cheapest_shop))
            customer.buy_products(next(shop
                                       for shop in shops
                                       if shop.name == cheapest_shop))
            customer.ride_home()
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
