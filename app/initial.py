import json

from app.customer import Customer

from app.shop import Shop

with open("app/config.json", "r") as file:
    data = json.load(file)


def to_init(file_name: file):
    """
    This function creates:
    -variable with the price per liter of fuel;
    -a list of users
    -list of shops
    """

    list_of_customers = []
    list_of_shops = []

    fuel_price = file_name["FUEL_PRICE"]

    for _ in file_name["customers"]:
        list_of_customers.append(Customer(_))

    for _ in file_name["shops"]:
        list_of_shops.append(Shop(_))

    return fuel_price, list_of_customers, list_of_shops


if __name__ == '__main__':
    price, list_customers, list_shops = to_init(data)
    print(price, list_customers[0].__dict__, list_shops[0].__dict__, sep="   ")
