import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    customers = Customer.create_customers(config_data)
    shops = Shop.create_shops(config_data)

    for customer in customers:
        customer.get_money()
        shop_costs = {}

        for shop in shops:
            shop_cost = round(
                shop.get_total_cost_per_store(customer, fuel_price), 2)
            shop_costs[shop_cost] = shop
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {shop_cost}")

        min_amount = min(shop_costs)

        if min_amount > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue

        target_shop_instance = shop_costs.get(min_amount)
        print(f"{customer.name} rides to {target_shop_instance.name}\n")
        customer.location = target_shop_instance.location
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer}, for your purchase!")
        print("You have bought:")

        order = customer.product_cart

        for product, qty in order.items():
            product_price = target_shop_instance.get_product_price(product)
            subtotal = product_price * qty

            if subtotal % 1 == 0:
                formatted_subtotal = "{:.0f}".format(subtotal)
            else:
                formatted_subtotal = subtotal

            formatted_line = (f"{qty} {product}s for"
                              f" {formatted_subtotal} dollars")
            print(formatted_line)

        print(f"Total cost is"
              f" {target_shop_instance.get_check_amount(order)}"
              f" dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        customer.money -= min_amount
        customer.location = customer.home_location
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
