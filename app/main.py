import json

if __name__ == "__main__":
    from customer import Customer
    from shop import Shop
else:
    from app.customer import Customer
    from app.shop import Shop


def shop_trip() -> None:
    config = None
    if __name__ == "__main__":
        config_filename = "config.json"
    else:
        config_filename = "./app/config.json"
    with open(config_filename, "rt") as config_file:
        config = json.load(config_file)

    if config:
        fuel_price = config.get("FUEL_PRICE", None)
        customers = []
        shops = []
        if "customers" in config:
            customers = Customer.get_list_customers(config["customers"])
        if "shops" in config:
            shops = Shop.get_list_shops(config["shops"])

        for customer in customers:
            customer.choose_cheapest_shop(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
