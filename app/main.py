from app.customer import Customer, read_from_json
from app.shop import Shop


def shop_trip() -> None:
    data_file = "app/config.json"
    # data_file = "config.json"

    data_customs = read_from_json(data_file, "customers")
    data_shop = read_from_json(data_file, "shops")
    fuel_price = read_from_json(data_file, "FUEL_PRICE")

    custom_list = []
    shop_list = []
    for _ in data_customs:
        custom_list.append(Customer.load_info_customer(_))
    for _ in data_shop:
        shop_list.append(Shop.load_info_shop(_))

    for custom_info in custom_list:
        print(custom_info.customer_shopping(shop_list, fuel_price))


if __name__ == "__main__":
    shop_trip()
