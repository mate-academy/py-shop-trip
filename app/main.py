from app.config_loader import load_config
from app.customer import Customer
from app.shop import Shop
import datetime


def shop_trip() -> None:
    config = load_config()
    customers_data = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        for customer in config["customers"]
    ]

    shop_data = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]
    fuel_price = config["FUEL_PRICE"]

    for customer in customers_data:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = None
        best_shop = None

        for shop in shop_data:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            if cost is not None:
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {round(cost, 2)}")

            if (cost is not None
                    and (min_cost is None or cost < min_cost)):
                min_cost = cost
                best_shop = shop

        if best_shop and min_cost <= customer.money:
            home_location = customer.location
            print(f"{customer.name} rides to {best_shop.name}")
            distance = customer.calculate_distance(
                customer.location, best_shop.location
            )
            customer.location = best_shop.location
            price_product = min_cost - (
                customer.car.calculate_cost_fuel(distance, fuel_price) * 2
            )

            customer.money -= min_cost
            print()
            print(
                f"Date: {datetime.datetime.now().strftime(
                    '%d/%m/%Y %H:%M:%S'
                )}"
            )
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, amount in customer.product_cart.items():
                product_cost = amount * best_shop.products[product]
                print(f"{amount} {product}s "
                      f"for {int(product_cost) if product_cost.is_integer(
                      ) else product_cost} dollars")
            print(f"Total cost is {round(price_product, 2)} dollars")
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} "
                  f"now has {round(customer.money, 2)} "
                  f"dollars")
            print()
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make "
                  f"a purchase in any shop")
