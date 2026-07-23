from app.config_loader import read_config, build_customers, build_shops


def shop_trip() -> None:
    config = read_config()
    fuel_price = config["FUEL_PRICE"]
    customers = build_customers(config)
    shops = build_shops(config)

    for index, customer in enumerate(customers):
        if index != 0:
            print()
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_cost = float("inf")
        cheapest_shop = None

        for shop in shops:
            trip_cost = customer.calculate_total_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

            if trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            print(f"{customer.name} rides home")
            customer.money -= cheapest_cost
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
