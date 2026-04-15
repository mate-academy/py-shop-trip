from app.shop import Shop


from app.customer import Customer


from app.utils import format_money


import json


def shop_trip() -> None:
    with open("config.json", "r") as f:
        data = json.load(f)
        customers = data["customers"]
        shops = data["shops"]
        fuel_price = data["FUEL_PRICE"]

    customer_objects = []
    for customer in customers:
        customer_objects.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
        )

    shop_objects = []
    for shop in shops:
        shop_objects.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"],
            )
        )

    for customer in customer_objects:
        best_shop = None
        best_cost = 100000000
        print(f"{customer.name} has "
              f"{format_money(customer.money)} dollars")
        for shop in shop_objects:
            shopping = customer.products_cost(shop)
            if shopping is None:
                continue
            cost = customer.trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost:.2f}")
            if cost < best_cost:
                best_cost = cost
                best_shop = shop
        if customer.money < best_cost:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
        else:
            original_location = customer.location.copy()
            print(f"{customer.name} rides to {best_shop.name}")
            travel = customer.travel_cost(best_shop, fuel_price)
            shopping = customer.products_cost(best_shop)
            customer.location = best_shop.location
            print()
            best_shop.print_receipt(customer.product_cart, customer.name)
            customer.location = original_location
            customer.update_money(shopping, travel)

            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{format_money(customer.money)} dollars")
            print()
