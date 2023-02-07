import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        user_and_shop_data = json.load(file)
    fuel_price = user_and_shop_data["FUEL_PRICE"]
    customers = [Customer.make_instance(customer) for customer
                 in user_and_shop_data["customers"]]
    shops = [Shop.make_instance(shop) for shop in user_and_shop_data["shops"]]
    is_first_customer = True
    for customer in customers:
        if not is_first_customer:
            print("")
        is_first_customer = False
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = customer.calculate_trip_costs(shops, fuel_price)
        if cheapest_shop != "not_enough_money":
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.print_bill(customer)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
