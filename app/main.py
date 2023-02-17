from app.read_file_json import read_json


def shop_trip() -> None:
    fuel_price, customers, shops = read_json()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        choice = None
        for shop in shops:
            has_money, result = customer.calc_price_to_shop(shop, fuel_price)
            if has_money and (not choice or result["cost"] < choice["cost"]):
                choice = result
        if not choice:
            print(f"{customer.name} doesn't have enough"
                  f" money to make purchase in any shop")
            continue
        customer.ride_to_shop(choice["name"], choice["cost"])
