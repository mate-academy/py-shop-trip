from app.customer import customers_list


def shop_trip() -> None:
    for customer in customers_list:
        customer.initial_amount()
        customer.price_of_trip()
