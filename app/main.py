from app.extract_json_data import extract_data_json
from app.customer_part.customer import Customer
from app.shop_part.shop import Shop
from app.customer_part.car import Car
from app.customer_part.find_shop import find_cheapest_shop


def shop_trip() -> None:
    Car.fuel_price, custemers_data, shops_data = extract_data_json()
    available_shops = [Shop.create_shop_from_dict(shops_data)]
    customers = Customer.create_users_from_list(custemers_data)
    find_cheapest_shop(customers, available_shops)


if __name__ == "__main__":
    shop_trip()
