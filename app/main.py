import json
import datetime
import os

from app.data import create_clients, create_shops


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as json_file:
        data = json.load(json_file)
    fuel_price = data["FUEL_PRICE"]

    clients = create_clients(data)
    shops = create_shops(data)

    for client_name, client_info in clients.items():
        print(f"{client_name} has {client_info.money} dollars")

        client_info.calculate_shopping_costs(shops, fuel_price)
        min_shop_name, min_shop_cost = min(
            client_info.shopping_costs.items(), key=lambda x: x[1]
        )

        if client_info.money < min_shop_cost:
            print(f"{client_name} doesn't have enough money to "
                  f"make a purchase in any shop")
            return
        home_location = client_info.location
        print(f"{client_name} rides to {min_shop_name}\n")


        client_info.location = shops[min_shop_name].location
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime(
            "Date: %d/%m/%Y %H:%M:%S"
        )
        print(formatted_datetime)
        print(f"Thanks, {client_name}, for your purchase!")
        purchase_price = shops[min_shop_name].process_purchase(client_info)
        print(f"Total cost is {purchase_price:.1f} dollars")
        print("See you again!\n")

        client_info.money -= min_shop_cost
        print(f"{client_name} rides home")
        client_info.location = home_location
        print(f"{client_name} now has {client_info.money:.2f} dollars\n")
