import json
from app.customer import create_customer
from app.shop import create_shops
from pathlib import Path


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as config_file:
        main_dict = json.load(config_file)
        customers_list = create_customer(main_dict["customers"])
        shops_list = create_shops(main_dict["shops"])
        fuel_price = main_dict["FUEL_PRICE"]
        for customer in customers_list:
            print(f"{customer.name} has {customer.money} dollars")
            best_shop, fuel_cost = customer.choose_shop(shops_list, fuel_price)
            if best_shop:
                customer.ride_to(best_shop)
                best_shop.purchase(customer)
                customer.money -= fuel_cost
                customer.ride_home(customer.home)


if __name__ == "__main__":
    shop_trip()
