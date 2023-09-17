import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    for customer_info in customers:
        customer = Customer(customer_info, fuel_price)
        print(f"{customer.name} has {customer.money} dollars")

        shop_objects = [Shop(shop) for shop in shops]
        affordable_shops = [shop for shop in shop_objects
                            if customer.calculate_trip_cost(shop.location)
                            <= customer.money]

        if not affordable_shops:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop\n")
            continue

        for shop in affordable_shops:
            trip_cost = customer.calculate_trip_cost(shop.location)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_cost:.2f}")

        cheapest_shop = min(affordable_shops, key=lambda shop: customer.
                            calculate_trip_cost(shop.location))
        customer.go_to_shop(cheapest_shop)
        customer.go_home()

        print(f"{customer.name} now has {customer.money:.2f} dollars\n")
