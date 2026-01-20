import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = []
    shops = []

    for data in config["customers"]:
        car = Car(data["car"]["brand"], data["car"]["fuel_consumption"])
        customer = Customer(
            data["name"],
            tuple(data["location"]),
            data["money"],
            data["product_cart"],
            car
        )
        customers.append(customer)

    for data in config["shops"]:
        shop = Shop(data["name"], tuple(data["location"]), data["products"])
        shops.append(shop)

    for i, customer in enumerate(customers):
        if i > 0:
            print()  # Add empty line before each customer except the first
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        lowest_cost = float("inf")

        for shop in shops:
            if shop.can_fulfill_cart(customer.product_cart):
                cost = shop.trip_cost(customer, fuel_price)
                print(f"{customer.name}'s trip to the {shop.name} costs "
                      f"{cost:.2f}")
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_shop = shop

        if best_shop and lowest_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.ride_to(best_shop.location)
            customer.purchase(best_shop.name, best_shop.products)
            print()  # Add empty line after purchase
            print(f"{customer.name} rides home")
            customer.ride_home()
            distance = customer.distance_to(best_shop.location)
            fuel_expense = customer.car.fuel_cost(distance, fuel_price) * 2
            customer.money -= fuel_expense
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  f"purchase in any shop")
