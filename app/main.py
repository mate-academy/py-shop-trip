import datetime
import json
from app.customer import Customer
from app.shop import Shop


def calculate_product_cost(product_cart: dict, products: dict) -> float:
    return sum(product_cart[product] * products[product]
               for product in product_cart)


def format_price(price: float) -> int | float:
    return int(price) if price % 1 == 0 else price


def shop_trip() -> None:
    with open("app/config.json") as data_file:
        all_data = json.load(data_file)

    customers = [
        Customer(**customer_data)
        for customer_data in all_data["customers"]
    ]
    shops = [Shop(**shop_data) for shop_data in all_data["shops"]]
    fuel_price = all_data["FUEL_PRICE"]

    for customer in customers:
        all_shops_cost = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            lap = ((customer.location[0] - shop.location[0]) ** 2
                   + (customer.location[1] - shop.location[1]) ** 2) ** 0.5
            costs = calculate_product_cost(customer.product_cart,
                                           shop.products)
            destination_cost = ((lap * customer.car["fuel_consumption"] / 100)
                                * 2 * fuel_price)
            total_cost = round(destination_cost + costs, 2)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_cost}")
            all_shops_cost[shop.name] = total_cost

        cheapest_shop_name = min(all_shops_cost, key=all_shops_cost.get)
        cheapest_shop = next(
            shop for shop in shops if shop.name == cheapest_shop_name
        )
        if all_shops_cost[cheapest_shop_name] > customer.money:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            continue

        products_cost = calculate_product_cost(
            customer.product_cart, cheapest_shop.products)
        money_left = customer.money - all_shops_cost[cheapest_shop_name]
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"{customer.name} rides to {cheapest_shop.name}\n\n"
              f"Date: {current_date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")

        for product, quantity in customer.product_cart.items():
            product_cost = quantity * cheapest_shop.products[product]
            print(f"{quantity} {product}s "
                  f"for {format_price(product_cost)} dollars")

        print(f"Total cost is {products_cost} dollars\n"
              "See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has {money_left} dollars\n")
