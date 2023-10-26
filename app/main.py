from app.utils.utils import (
    file_handler,
    init_customers,
    init_shops,
    visit_shop
)


def shop_trip() -> None:
    config_data, fuel_price = file_handler("app/config.json")

    shops = init_shops(config_data)

    customers = init_customers(config_data)

    visit_shop(customers, shops, fuel_price)
