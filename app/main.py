import json
import datetime
import math
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        user_data = json.load(config)

    customers_data = user_data["customers"]
    shops = user_data["shops"]
    price_of_fuel = user_data["FUEL_PRICE"]

    customers = []
    for customer_data in customers_data:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"],
        )

        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            money=customer_data["money"],
            car=car,
            customer_location=customer_data["location"],
        )
        customers.append(customer)

    shops = [Shop(**shop_data) for shop_data in shops]

    for customer in customers:
        customer.has_money()

        trip_costs = []
        purchase_costs = []

        for shop in shops:
            total_cost = customer.prod_cost(shop.products) + (
                customer.car.cost_of_fuel(
                    customer.customer_location, shop.location, price_of_fuel
                )
            )
            trip_costs.append(total_cost)
            purchase_costs.append(customer.prod_cost(shop.products))

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost}")

        cheapest_trip = {
            "cost": min(trip_costs),
            "shop": shops[trip_costs.index(min(trip_costs))],
        }

        if customer.money < cheapest_trip["cost"]:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            now_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(
                f"{customer.name} rides to {cheapest_trip['shop'].name}\n\n"
                f"Date: {now_time}\n"
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought: "
            )
            cost_of_products = []
            for product, quantity in customer.product_cart.items():
                price = cheapest_trip["shop"].products.get(product, 0)
                cost = price * quantity
                if isinstance(cost, float) and cost.is_integer():
                    cost = math.floor(cost)
                cost_of_products.append(cost)
                print(f"{quantity} {product}s for {cost} dollars")
            print(
                f"Total cost is {sum(cost_of_products)} dollars\n"
                f"See you again!\n\n"
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{customer.money-cheapest_trip['cost']} dollars\n"
            )


if __name__ == "__main__":
    shop_trip()
