from __future__ import annotations
from json import load
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    # Getting data from file:
    with open("app/config.json") as config_file:
        config = load(config_file)
    fuel_price = config["FUEL_PRICE"]
    shop_list = Shop.create_shops_list(config["shops"])
    customers = Customer.create_customer_list(config["customers"])

    for customer in customers:
        # Check for products availability
        shops_with_products = customer.check_products_availability(
            shop_list
        )
        # Calculate trip cost for each of shop
        shops_trip_cost = customer.calculate_trip_cost(
            shops_with_products,
            fuel_price
        )

        # Choosing cheapest shop trip
        print(f"{customer.name} has {customer.money} dollars")
        for cost, shop in shops_trip_cost.items():
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        if shops_trip_cost:
            min_trip_cost = min(shops_trip_cost.keys())
            if customer.money < min_trip_cost:
                print(f"{customer.name} \
doesn't have enough money to make a purchase in any shop")
                continue

            cheapest_shop = shops_trip_cost[min_trip_cost]
            customer_home = customer.location
            one_way_drive_cost = customer.car.calculate_drive_cost(
                customer.location, cheapest_shop.location,
                fuel_price
            )

            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location
            customer.money -= one_way_drive_cost

            cart_cost = cheapest_shop.print_receipt(
                customer.product_cart,
                customer.name
            )
            customer.money -= cart_cost

            print(f"\n{customer.name} rides home")
            customer.location = customer_home
            customer.money -= one_way_drive_cost

            print(f"{customer.name} now has {customer.money} dollars\n")


shop_trip()
