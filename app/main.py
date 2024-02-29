from app.customer import Customer
from app.statics_methods import Method
from app.shop import Shop


def shop_trip() -> None:
    json_data = Method.open_file("app/config.json")
    for element in json_data["customers"]:
        customer = Customer(element)
        customer.print_money()
        shop_data = customer.customer_trip_to_shops(json_data)
        if not customer.check_perf_purchase(shop_data, json_data):
            return
        list_prod = Method.transform_in_plural(
            list(customer.product_cart.keys()))
        shop = Shop(json_data["shops"][shop_data[1][1]])
        shop.print_purchase(customer, shop_data, list_prod)
