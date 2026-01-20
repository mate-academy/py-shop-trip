import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        file_config = json.load(file)

    for customer in file_config["customers"]:
        buyer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["fuel_consumption"]
        )

        buyer.print_customer_name_and_money()

        shops_and_prices = {}
        instance_shops = []
        for shop in file_config["shops"]:
            shop = Shop(shop["name"], shop["location"], shop["products"])
            price = buyer.get_price_product_cart(shop, file_config)
            shops_and_prices[shop.name] = price
            instance_shops.append({shop.name: shop})
        name_shop_whit_best_price = min(
            shops_and_prices, key=shops_and_prices.get
        )
        best_price = shops_and_prices[name_shop_whit_best_price]
        instance_shop_whit_best_price = None
        for instance_shop in instance_shops:
            if name_shop_whit_best_price in instance_shop:
                instance_shop_whit_best_price = (
                    instance_shop.get(name_shop_whit_best_price)
                )
        if buyer.money < best_price:
            print(
                f"{buyer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            buyer.change_location_buyer(instance_shop_whit_best_price)
            buyer.print_check(instance_shop_whit_best_price)
            buyer.calculate_buyer_balance_of_money(best_price)
