from app.utils.utils import (
    file_handler,
    get_customers,
    get_shops,
    visit_shop
)


def shop_trip() -> None:
    fuel_price, customers_data, shops_data = file_handler("app/config.json")

    shops = get_shops(shops_data)

    customers = get_customers(customers_data)

    visit_shop(customers, shops, fuel_price)
