from app.dataloader import Dataloader
from app.customers import Customer


def shop_trip() -> None:
    Dataloader("config.json")
    for customer in Customer.customers:
        customer.do_shop_trip()
