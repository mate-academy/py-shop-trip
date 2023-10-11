from app import get_data


def shop_trip() -> None:
    customers, shops, fuel_price = get_data("config.json")
    for customer in customers:
        cheapest_shop, cost = customer.calculate_trip_cost(shops,
                                                           fuel_price)
        customer.trip_to_cheapest(cheapest_shop, cost)


shop_trip()
