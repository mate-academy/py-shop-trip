from app.customer import Customer
import datetime


class Shop:
    def __init__(
        self, name: str, location: list[int, int], products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name

    def serve_customer(self, customer: Customer) -> None:
        d = datetime.datetime
        print(d)