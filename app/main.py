from app.customer import Customer
from app.shop import Shop
from app.utils import load_config


def shop_trip() -> None:
    """
    Reads config, initializes customers and shops, calculates the
    cheapest trip for each customer, and simulates the purchase
    if the customer can afford it.
    """
    config = load_config()

    if config is None:
        return

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(s["name"], s["location"], s["products"])
        for s in config["shops"]
    ]

    customers = [
        Customer(
            c["name"],
            c["product_cart"],
            c["location"],
            c["money"],
            c["car"],
            fuel_price
        )
        for c in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_trip_cost = float("inf")
        best_shop = None

        for shop in shops:
            trip_cost = customer.calculate_total_trip_cost(shop)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_cost:.2f}")

            if trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                best_shop = shop

        if cheapest_trip_cost <= customer.money:
            customer.ride_to_shop(best_shop)
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  f"purchase in any shop")


if __name__ == "__main__":
    shop_trip()
