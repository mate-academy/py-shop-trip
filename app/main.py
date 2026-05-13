import datetime
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    for index, customer_data in enumerate(config["customers"]):
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                brand=customer_data["car"]["brand"],
                fuel_consumption=customer_data["car"]["fuel_consumption"]
            )
        )

        if index > 0:
            print()

        print(f"{customer.name} has {customer.money} dollars")

        best_cost = float("inf")
        best_shop = None

        for shop_data in config["shops"]:
            shop = Shop(
                name=shop_data["name"],
                location=shop_data["location"],
                products=shop_data["products"]
            )
            trip_cost = round(customer.calculate_shopping_cost(shop), 2)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )

            if trip_cost < best_cost and trip_cost <= customer.money:
                best_cost = trip_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}")
            print()

            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():
                if product in best_shop.products:
                    product_cost = best_shop.products[product] * quantity
                    product_cost = int(product_cost) \
                        if product_cost == int(product_cost)\
                        else product_cost
                    print(f"{quantity} {product}s for {product_cost} dollars")

            total_cost = customer.calculate_products_cost(best_shop)
            total_cost = int(total_cost)\
                if total_cost == int(total_cost)\
                else total_cost
            print(f"Total cost is {total_cost} dollars")
            print("See you again!")
            print()

            print(f"{customer.name} rides home")
            customer.money -= best_cost
            final_money = round(customer.money, 2)
            print(f"{customer.name} now has {final_money} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
