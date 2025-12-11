from app.creating_classes import (creation_class_customer,
                                  creation_class_shop)


def shop_trip() -> None:
    customers = creation_class_customer()
    shops = creation_class_shop()

    for customer in customers:
        customer.customer_money()
        shops_prices = customer.purchase_amount(shops)
        best_shop = customer.best_shop(shops_prices)
        customer.trip_to_the_stor(best_shop)
