from app.parser import Parser
import os


def shop_trip() -> None:
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "config.json")
    parser = Parser(path)
    shops = parser.parse_shops()
    customers = parser.parse_customers()
    for customer in customers:
        customer.begin_shopping(shops)
