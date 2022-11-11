import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        full_dict = json.load(file)

    for sh in full_dict["shops"]:
        shop = Shop(sh)
        shop.add_to_shop_list()
    shop_list = Shop.shop_list

    for one_customer in full_dict["customers"]:
        buyer = Customer(one_customer)
        print(f"{buyer.name} has {buyer.money} dollars")
        buyer.find_best_shop(shop_list, full_dict["FUEL_PRICE"])


if __name__ == "__main__":
    shop_trip()
