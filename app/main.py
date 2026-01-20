from app.config import config
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    for customer_data in config["customers"]:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=customer_data["name"],
            location=customer_data["location"],
            money=customer_data["money"],
            product_cart=customer_data["product_cart"],
            car=car
        )

        print(f"{customer.name} has {customer.money} dollars")
        best_shop, best_cost = None, float("inf")

        for shop_data in config["shops"]:
            shop = Shop(
                name=shop_data["name"],
                location=shop_data["location"],
                products=shop_data["products"]
            )

            distance = customer.calculate_distance(shop.location)
            trip_cost = customer.calculate_fuel_cost(distance)
            product_cost = shop.calculate_total_cost(customer.product_cart)
            total_cost = trip_cost + product_cost

            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} costs {total_cost:.2f}"
            )

            if total_cost < best_cost and total_cost <= customer.money:
                best_shop, best_cost = shop, total_cost

        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.make_purchase(best_shop)
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        customer.return_home()
