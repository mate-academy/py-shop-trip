import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json") as config:
        infos = json.load(config)

    fuel_price = infos["FUEL_PRICE"]

    for item in infos["customers"]:
        customer = Customer(
            item["name"],
            item["product_cart"],
            item["location"],
            item["money"],
        )
        customer.customer_info()
        cars = Car(item["car"]["brand"], item["car"]["fuel_consumption"])
        shop_dict = {}
        for shop in infos["shops"]:
            current_shop = 0
            shop = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            current_shop += sum(shop.count_product(customer.product_cart))
            current_shop += round(
                (cars.fuel_cost(customer.location, shop.location, fuel_price)
                 * 2)
                , 2)
            customer.shop_visit(shop.name, current_shop)
            shop_dict[current_shop] = shop

        cheapest_shop = shop_dict[min(shop_dict.keys())]
        if min(shop_dict.keys()) <= customer.money:
            customer.change_location(cheapest_shop.location)
            cheapest_shop.bill(customer.name, customer.product_cart)
            customer.come_back_home(min(shop_dict.keys()))
            customer.change_location(item["location"])
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
