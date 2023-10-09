from app import get_data


def shop_trip() -> None:
    customer_list, shop_list, fuel_price = get_data("config.json")
    for customer in customer_list:
        cheapest_shop, cost = customer.calculate_trip_cost(shop_list,
                                                           fuel_price)
        customer.trip_to_cheapest(cheapest_shop, cost)


shop_trip()
