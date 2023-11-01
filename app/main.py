import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app import parsing


def shop_trip() -> None:
    config = parsing.parse_data_from_json()
    customers_data = config["customers"]
    shops_data = config["shops"]

    for customer_data in customers_data:
        car_data = customer_data.get("car")

        customer = Customer(
            customer_data["name"],
            customer_data["location"],
            customer_data["money"],
            customer_data["product_cart"],
            Car(car_data["brand"], car_data["fuel_consumption"])
        )

        cheapest_cost = float("inf")
        best_shop = None

        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        for shop_data in shops_data:
            shop = Shop(**shop_data)
            product_cost = customer.calculate_product_cost(shop)
            fuel_cost = customer.calculate_fuel_cost(customer.car, shop)
            total_cost = round(product_cost + fuel_cost, 2)

            print(f"{customer.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost < cheapest_cost and customer.money >= total_cost:
                cheapest_cost = total_cost
                best_shop = shop

        if best_shop:
            customer.calculate_fuel_cost(customer.car, best_shop)
            print(f"{customer.name} rides to {best_shop.name}\n")
            print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for item, quantity in customer.product_cart.items():
                cost = best_shop.products.get(item, 0) * quantity
                print(f"{quantity} {item}s for {round(cost, 2)} dollars")
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")

            customer.money -= cheapest_cost

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop\n")


if __name__ == "__main__":
    shop_trip()
