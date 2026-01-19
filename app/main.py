import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = []
    shops = []

    for shop_data in config["shops"]:
        shops.append(Shop(**shop_data))

    for customer_data in config["customers"]:
        car = Car(**customer_data.pop("car"))
        customers.append(Customer(**customer_data, car=car))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        best_cost = float("inf")

        for shop in shops:
            trip_cost, distance = shop.calculate_trip_cost(
                customer.location,
                fuel_price,
                customer.car.fuel_consumption
            )

            product_cost, _ = shop.purchase(
                customer.name, customer.product_cart
            )
            total_cost = trip_cost + product_cost

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {round(total_cost, 2)}")
            if total_cost < best_cost and total_cost <= customer.money:
                best_cost = total_cost
                best_shop = shop

        if best_shop:
            trip_cost, _ = best_shop.calculate_trip_cost(
                customer.location,
                fuel_price,
                customer.car.fuel_consumption
            )
            customer.money -= best_cost
            customer.move_to(best_shop.location)

            print(f"{customer.name} rides to {best_shop.name}\n")
            product_cost, receipt = best_shop.purchase(
                customer.name, customer.product_cart
            )
            print(receipt)

            trip_home_cost, _ = best_shop.calculate_trip_cost(
                customer.location,
                fuel_price,
                customer.car.fuel_consumption
            )
            original_location = customer.location
            customer.money -= trip_home_cost
            customer.move_to(original_location)

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
