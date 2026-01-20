from app.read_data import create_customer_objects, create_shop_objects


def shop_trip() -> None:
    customers = create_customer_objects()
    shops = create_shop_objects()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = shops[0]
        for shop in shops:
            coast_of_the_trip = customer.cost_of_the_trip(
                shop, customer.car.fuel_price
            )
            if customer.cost_of_the_trip(
                    cheapest_shop,
                    customer.car.fuel_price
            ) > coast_of_the_trip:
                cheapest_shop = shop
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(coast_of_the_trip, 2)}")

        customer.go_to_the_shop(cheapest_shop)
