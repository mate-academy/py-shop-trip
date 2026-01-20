import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config_data = json.load(config)
    fuel_price = config_data["FUEL_PRICE"]
    customers = [
        Customer(**customer_data) for customer_data in config_data["customers"]
    ]
    shops = [
        Shop(**shop_data, fuel=fuel_price)
        for shop_data in config_data["shops"]
    ]
    result_message = ""
    for customer in customers:
        result_message += f"{customer.name} has {customer.money} dollars\n"
        store_price = []
        for shop in shops:
            price = customer.calculate_trip_cost(shop)
            store_price.append((shop.name, price, shop))
            result_message += (
                f"{customer.name}'s " f"trip to "
                f"the {shop.name} costs {price}\n"
            )
        smallest_price_tuple = min(store_price, key=lambda x: x[1])
        if smallest_price_tuple[1] <= customer.money:
            result_message += (
                f"{customer.name} rides " f"to {smallest_price_tuple[0]}\n\n"
            )
            customer.money -= smallest_price_tuple[1]
        else:
            result_message += (
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue
        result_message += (
            "Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:\n"
        )
        shop = smallest_price_tuple[2]
        for product, quantity in customer.product_cart.items():
            price = shop.products[product] * quantity
            if price == int(price):
                price = int(price)
            result_message += f"{quantity} {product}s " \
                              f"for {price} dollars\n"
        result_message.rstrip("\n")
        total = customer.calculate_product_cost(shop)
        result_message += (
            f"Total cost is {total} dollars\n"
            f"See you again!\n"
            "\n"
            f"{customer.name} rides home\n"
            f"{customer.name} now "
            f"has {customer.money} dollars\n\n"
        )
    print(result_message)
