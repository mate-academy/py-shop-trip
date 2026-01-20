from app.functions import read_info_from_json


def shop_trip():
    data = read_info_from_json()
    for customer in data["list_of_customers"]:
        customer.choose_the_shop(data["list_of_shops"], data["fuel_cost"])
