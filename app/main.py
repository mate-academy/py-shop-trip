import json

from app.data_handler import (
    add_models,
    calculate_distance,
    calculate_fuel_cost,
    create_check
)


def shop_trip() -> None:
    result = {}

    with open("app/config.json", encoding="utf-8") as file:
        config = json.load(file)
    data = add_models(config)

    for customer in data["customers"]:
        result[customer] = {}
        for shop in data["shops"]:
            spent_money = 0
            check = ""
            distance = calculate_distance(customer.location, shop.location) * 2
            spent_money += calculate_fuel_cost(distance,
                                               customer.car.fuel_consumption,
                                               config["FUEL_PRICE"])

            total_cost = 0
            for name, quantity in customer.product_cart.items():
                spent = shop.products[name] * quantity
                check += f"{quantity} {name}s for " \
                         f"{int(spent) if spent == int(spent) else spent} " \
                         f"dollars\n"
                total_cost += spent
            spent_money += total_cost

            check += f"Total cost is {total_cost} dollars\n"
            result[customer][shop.name] = [round(spent_money, 2), check]

    for customer, shops in result.items():
        print(create_check(customer, shops))
