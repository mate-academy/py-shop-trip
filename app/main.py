from app.utils import load_config
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config = load_config("app/config.json")
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in config["shops"]
    ]
    fuel_price = config["FUEL_PRICE"]

    for customer_dict in config["customers"]:

        customer = Customer(
            name=customer_dict["name"],
            location=customer_dict["location"],
            money=customer_dict["money"],
            product_cart=customer_dict["product_cart"],
            car_data=customer_dict["car"]
        )
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_trip = None
        best_shop = None

        for shop in shops:

            trip_cost = (
                customer.calculate_trip_cost(shop, fuel_price))

            if trip_cost is not None:
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {trip_cost:.2f}")
            total_cost = trip_cost
            if total_cost is not None and customer.money >= total_cost:
                if cheapest_trip is None or total_cost < cheapest_trip:
                    cheapest_trip = total_cost
                    best_shop = shop

        if best_shop:
            trip_cost = customer.calculate_trip_cost(best_shop, fuel_price)
            customer.make_purchase(best_shop, trip_cost)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
