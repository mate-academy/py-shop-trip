import json
from pathlib import Path

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    base_dir = Path(__file__).resolve().parent

    with open(base_dir / "config.json", "r") as input_data_file:
        input_data = json.load(input_data_file)
        customers = input_data["customers"]
        fuel_price = input_data["FUEL_PRICE"]
        shops = input_data["shops"]

        customer_instance_list = []

        for customer in customers:
            customer = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"],
            )
            customer_instance_list.append(customer)

        shop_instance_list = []

        for shop in shops:
            shop = Shop(
                shop["name"],
                shop["location"],
                shop["products"],
            )
            shop_instance_list.append(shop)

        for customer in customer_instance_list:

            cheapest_shop = customer.shop_to_go(
                customer.car, shop_instance_list, fuel_price
            )

            if cheapest_shop is not None:
                cheapest_shop.print_purchase_receipt(customer)
                customer.customer_rides_home(
                    customer.car, cheapest_shop, fuel_price
                )
