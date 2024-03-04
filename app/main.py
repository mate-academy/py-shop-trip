from app.customer import customers
from app.shop import shops
from app.cost_calculation import choose_shop


def shop_trip() -> None:

    for customer in customers:
        choose_shop(customer, shops)
