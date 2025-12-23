import json

from app.customer import Customer

from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customer_list = [Customer(customer) for customer in data["customers"]]
        shop_list = [Shop(shop) for shop in data["shops"]]

        for customer in customer_list:
            print(f"{customer.name} has {customer.money} dollars")
            customer.choose_shop(shop_list, fuel_price)
            if not customer.best_shop:
                return
            else:
                customer.best_shop.print_receipt(customer)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has "
                      f"{customer.money - customer.best_price} dollars\n")
