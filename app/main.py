from app.customer import Customer
from app.shop import Shop
from app.utils import load_info


def shop_trip() -> None:
    config = load_info("config.json")
    if config is None:
        return
    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]
    customers = [
        Customer(
            cust["name"],
            cust["product_cart"],
            cust["location"],
            cust["money"],
            cust["car"]
        )
        for cust in config["customers"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        valid_trip_cost = {}
        for shop in shops:
            total_trip_cost = customer.calculate_trip_cost(
                shop.location, shop.product, fuel_price
            )
            if total_trip_cost is not None:
                print(f"{customer.name}'s"
                      f" trip to the {shop.name}"
                      f" costs {total_trip_cost}")
                valid_trip_cost[shop] = total_trip_cost
        if not valid_trip_cost:
            print(f"{customer.name} cannot buy all products in any shop.\n")
            continue
        best_shop = min(valid_trip_cost, key=valid_trip_cost.get)
        min_cost = valid_trip_cost[best_shop]
        if customer.money >= min_cost:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.location = best_shop.location
            products_only_cost = customer.calculate_products_cost(
                best_shop.product
            )
            best_shop.print_receipt(
                customer.name,
                customer.product_cart,
                products_only_cost
            )

            customer.money -= min_cost

            customer.location = customer.home_location

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {round(customer.money, 2)} dollars\n")

        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop"
                  )
