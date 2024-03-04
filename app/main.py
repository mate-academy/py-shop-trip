from app.customer import create_customers
from app.shop import create_shops
from app.cost_calculation import choose_shop
from app.data_loading import data_loading


def shop_trip() -> None:

    configs = data_loading()

    customers = create_customers(configs)
    shops = create_shops(configs)

    for customer in customers:
        choose_shop(customer, shops)
