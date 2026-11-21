def shop_trip() -> None:
    import json
    from pathlib import Path

    from app.car import Car
    from app.customer import Customer
    from app.shop import Shop

    config_path = Path(__file__).resolve().parent / "config.json"

    with config_path.open("r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"],
        )
        for shop_data in config["shops"]
    ]

    customers = [
        Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                brand=customer_data["car"]["brand"],
                fuel_consumption=(
                    customer_data["car"]["fuel_consumption"]
                ),
            ),
        )
        for customer_data in config["customers"]
    ]

    for customer_index, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money:g} dollars")

        shop_trip_costs = []

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(
                shop,
                fuel_price,
            )
            shop_trip_costs.append((shop, trip_cost))

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {trip_cost:.2f}"
            )

        cheapest_shop, cheapest_cost = min(
            shop_trip_costs,
            key=lambda shop_cost: shop_cost[1],
        )

        if customer.money >= cheapest_cost:
            customer.make_purchase(
                cheapest_shop,
                cheapest_cost,
            )
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        if customer_index < len(customers) - 1:
            print()
