from app.customer import Customer
from app.car import Car
from app.shop import Shop
import json


def shop_trip() -> None:
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers = []
    for customer_data in config_data["customers"]:
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            Car(
                customer_data["car"]["brand"],
                customer_data["car"]["fuel_consumption"]
            )
        )
        customers.append(customer)

    shops = []
    for shop_data in config_data["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(
                shop.get_location(),
                fuel_price
            )
            purchase_cost = shop.calculate_purchase_cost(
                customer.product_cart
            )

            if (
                    trip_cost + purchase_cost < cheapest_cost
                    and customer.money >= (trip_cost + purchase_cost)
            ):
                cheapest_cost = trip_cost + purchase_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.update_location(cheapest_shop.get_location())
            purchase_cost = cheapest_shop.calculate_purchase_cost(
                customer.product_cart
            )
            customer.make_purchase(
                cheapest_shop.name,
                cheapest_shop.products,
                customer.product_cart
            )
            customer.update_money(cheapest_cost, purchase_cost)
            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart,
                purchase_cost
            )
            customer.update_location(customer.location)

        print(f"{customer.name} now has "
              f"{customer.get_remaining_money()} dollars")


if __name__ == "__main__":
    shop_trip()
