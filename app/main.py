import math

from app.services.io import load_config
from app.models.shop import Shop
from app.models.customer import Customer
from app.models.car import Car
from app.services.pricing import trip_cost


def shop_trip() -> None:
    shop_trip_data = load_config("app/config.json")
    fuel_price = shop_trip_data["FUEL_PRICE"]
    shops_data = shop_trip_data["shops"]
    customers_data = shop_trip_data["customers"]
    shops = []
    for shop in shops_data:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))
    customers = []
    for customer in customers_data:
        customers.append(Customer(customer["name"], customer["product_cart"],
                                  customer["location"], customer["money"],
                                  Car(customer["car"]["brand"],
                                      customer["car"]["fuel_consumption"])))
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_candidates = []
        for index, shop in enumerate(shops):
            cost = trip_cost(customer, shop, fuel_price)
            print(f"{customer.name}'s trip to the"
                      f" {shop.name} costs {cost:.2f}")
            if isinstance(cost, (int, float)) and math.isfinite(cost):
                shop_candidates.append((cost, index, shop))
        if shop_candidates is None:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        else:
            best_cost, _, best_shop = min(shop_candidates)
            if customer.can_afford(best_cost):
                print(f"{customer.name} rides to {best_shop.name}")
                original_location = customer.location.copy()
                customer.move_to(best_shop.location)
                best_shop.print_receipt(customer)
                customer.money -= best_cost
                customer.move_to(original_location)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money:.2f} dollars")
                print()
            else:
                print(f"{customer.name} doesn't have enough money"
                        f" to make a purchase in any shop")
