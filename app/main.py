from app import car, customer, shop


def shop_trip() -> None:
    list_of_customers = customer.customer_create_list()
    list_of_shops = shop.shop_create_list()
    car.gas_trip_cost(list_of_customers, list_of_shops)
    customer.customer_calculations(list_of_customers, list_of_shops)
    customer.receipts(list_of_customers, list_of_shops)
