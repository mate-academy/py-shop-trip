from app.car import Car
import app.json_tools


def shop_trip() -> None:
    content = app.json_tools.read_file("app/config.json", "r")
    Car.fuel_price = content["fuel_price"]
    customer_instances = content["customers"]
    shop_instances = content["shops"]

    for customer in customer_instances:
        print(f"{customer.name} has {customer.money} dollars")
        cheaper_shop = None
        min_money_amount = customer.money

        for shop in shop_instances:

            total_money = customer.calculate_total_money(shop)
            if total_money <= min_money_amount:
                min_money_amount = total_money
                cheaper_shop = shop

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_money}")

        if cheaper_shop is None:
            print(f"{customer.name} doesn't have enough money "
                  "to make a purchase in any shop")
            continue

        customer.go_to_shop(cheaper_shop, min_money_amount)
