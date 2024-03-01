from app.data_processing import data_processing, customers
from app.choose_shop import chose_shop


def shop_trip() -> None:

    data_processing()

    for customer in customers:
        chose_shop(customer)
