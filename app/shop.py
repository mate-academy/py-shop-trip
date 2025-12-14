from app.configuration import config
from app.customers import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = [Customer(**customer_data) for
                 customer_data in config["customers"]]
    shops = [Shop(shop_data["name"],
                  shop_data["location"], shop_data["products"])
             for shop_data in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_prices = {}

        for shop in shops:
            cost = customer.shopping_cost_in(shop)
            if cost is not None:
                cost_str = f"{cost:.2f}".rstrip("0").rstrip(".")
                if shop.name.startswith("Shop '"):
                    print(f"{customer.name}'s "
                          f"trip to {shop.name} costs {cost_str}")
                else:
                    print(f"{customer.name}'s trip "
                          f"to the {shop.name} costs {cost_str}")
                trip_prices[shop] = cost

        if not trip_prices:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in "
                "any shop"
            )
            continue

        shop_to_go = min(trip_prices, key=trip_prices.get)
        min_cost = trip_prices[shop_to_go]

        if customer.money < min_cost:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in "
                "any shop"
            )
            continue

        print(f"{customer.name} rides to {shop_to_go.name}")
        customer.location = shop_to_go.location[:]

        shop_to_go.receipt(customer)

        print(f"{customer.name} rides home")
        customer.money -= min_cost
        customer.money = round(customer.money, 2)
        money_str = f"{customer.money:.2f}".rstrip("0").rstrip(".")
        print(f"{customer.name} now has {money_str} dollars\n")
