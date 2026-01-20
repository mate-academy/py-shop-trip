from app.customer import Customer
from app.shop import Shop
from app.utils import load_config


def shop_trip() -> None:
    config = load_config("config.json")
    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = [Customer(**data) for data in customers_data]
    shops = [Shop(**data) for data in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = float("inf")
        best_shop = None
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {trip_cost:.2f}"  # noqa E231
            )
            if trip_cost < min_cost:
                min_cost = trip_cost
                best_shop = shop

        if best_shop and min_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}\n")

            original_location = customer.location
            customer.location = best_shop.location
            customer.money -= min_cost
            best_shop.print_receipt(customer)
            print(f"{customer.name} rides home")

            customer.location = original_location
            print(
                f"{customer.name} now has {customer.money:.2f} "  # noqa E231
                f"dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
