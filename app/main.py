from app import dataloader


def shop_trip() -> None:
    data = dataloader.load_file("config.json")
    customers = dataloader.create_customers(data)
    fuel_price = data["FUEL_PRICE"]
    shops = dataloader.create_shops(data)

    for customer in customers:
        customer.do_shop_trip(shops, fuel_price)
