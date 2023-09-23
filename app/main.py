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

        car = Car(brand=customer_data["car"]["brand"],
                  fuel_consumption=customer_data["car"]["fuel_consumption"])

        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            money=customer_data["money"],
            car=car,
            customer_location=customer_data["location"]
        )
        customers.append(customer)

    shops_list = []
    for shop_data in shops:
        shop = Shop(name=shop_data["name"],
                    shop_location=shop_data["location"],
                    products=shop_data["products"])
        shops_list.append(shop)

    for customer in customers:
        customer.has_money()

        trip_costs = []
        purchase_costs = []

        for shop in shops_list:
            total_cost = \
                (customer.prod_cost(shop.products) + customer.car.cost_of_fuel(
                    customer.customer_location,
                    shop.shop_location,
                    price_of_fuel))
            trip_costs.append(total_cost)
            purchase_costs.append(customer.prod_cost(shop.products))

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

        cheapest_trip_cost = min(trip_costs)
        cheapest_trip_shop = shops_list[trip_costs.index(cheapest_trip_cost)]

        if customer.money < cheapest_trip_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_trip_shop.name}")
            now_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {now_time}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            cost_of_products = []
            for product, quantity in customer.product_cart.items():
                price = cheapest_trip_shop.products.get(product, 0)
                cost = price * quantity
                if isinstance(cost, float) and cost % 1 == 0.0:
                    cost = math.floor(cost)
                cost_of_products.append(cost)
                print(f"{quantity} {product}s for {cost} dollars")
            print(f"Total cost is {sum(cost_of_products)} dollars")
            print("See you again!")
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money-cheapest_trip_cost} dollars\n")


if __name__ == "__main__":
    shop_trip()
