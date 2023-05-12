import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json") as config:
        infos = json.load(config)

    fuel_price = infos["FUEL_PRICE"]
    shops_dict = {
        shop["name"]: Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in infos["shops"]
    }
    customers_dict = {
        customer["name"]: Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["fuel_consumption"]
        ) for customer in infos["customers"]
    }

    for customer in customers_dict.values():
        customer.customer_info()
        cheapest_shop = 1000
        for shop in shops_dict.values():
            current_shop = sum(shop.count_product(customer.product_cart))
            current_shop += round(
                (customer.fuel_cost(shop.location, fuel_price) * 2), 2)
            customer.shop_visit(shop.name, current_shop)
            if current_shop < cheapest_shop:
                cheapest_shop = current_shop
                customer.shop = shop

        if cheapest_shop <= customer.money:
            customer.change_location(customer.shop.location)
            customer.shop.bill(customer.name, customer.product_cart)
            customer.come_back_home(cheapest_shop)
            customer.change_location(customer.home)
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
