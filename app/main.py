from app.customer_trip import Customer


def shop_trip() -> None:
    Customer(Customer.open_file("../app/config.json")).customer_trip()
