import datetime

from app.utils import (load_config,
                       distance_between_locations,
                       price_for_trip,
                       all_cart_price)
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []
    config = load_config("app/config.json")
    for customer in config["customers"]:
        car = Car(**customer["car"])
        cust = Customer(customer["name"],
                        customer["product_cart"],
                        customer["location"],
                        customer["money"],
                        car)
        customers.append(cust)
    for shop_data in config["shops"]:
        shop = Shop(**shop_data)
        shops.append(shop)
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_price = float("inf")
        shop_to_visit = None
        for shop in shops:
            distance = distance_between_locations(customer.location,
                                                  shop.location)
            money_for_trip = price_for_trip(distance,
                                            customer.car.fuel_for_one_km(),
                                            config["FUEL_PRICE"]) * 2
            cart_price = all_cart_price(customer.product_cart,
                                        shop.products)
            full_price = money_for_trip + cart_price
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {full_price:.2f}")

            if customer.money >= full_price:
                if full_price < cheapest_price:
                    cheapest_price = full_price
                    shop_to_visit = shop

        if shop_to_visit is not None:
            home_location = customer.location.copy()
            customer.location = shop_to_visit.location
            visit_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            customer.money -= cheapest_price
            print(f"{customer.name} rides to {shop_to_visit.name}\n")
            print(f"Date: {visit_time}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  f"You have bought:")
            for product, count in customer.product_cart.items():
                print(f"{count} {product}s for "
                      f"{count * shop_to_visit.products[product]:g} dollars")
            cart_price = all_cart_price(
                customer.product_cart,
                shop_to_visit.products
            )

            print(f"Total cost is {cart_price} dollars\n"
                  f"See you again!\n"
                  f"\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{customer.money:.2f} dollars\n")
            customer.location = home_location
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
