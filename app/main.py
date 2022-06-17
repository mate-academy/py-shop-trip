import json
import datetime
from app.car.car import Car
from app.client.client import Client
from app.shop.shop import Shop


def shop_trip():
    with open('app/config.json', 'r') as file_data:
        file_data = json.load(file_data)

    list_costumer = [Client(name=client["name"],
                            product_cart=client["product_cart"],
                            location=client["location"],
                            money=client["money"],
                            car=Car(client["car"]["brand"],
                                    client["car"]["fuel_consumption"])
                            ) for client in file_data['customers']]

    list_shops = [Shop(name=shop["name"],
                       location=shop["location"],
                       products=shop["products"])
                  for shop in file_data["shops"]]

    for client in list_costumer:
        print(f"{client.name} has {client.money} dollars")
        choose_shop = {}

        for shop in list_shops:
            total_shop = client.purchase_at_shop(shop)
            total_road = client.price_for_road(file_data["FUEL_PRICE"], shop)
            main_total = round(total_road + total_shop + total_road, 2)
            print(f"{client.name}'s trip to the"
                  f" {shop.name} costs {main_total}")
            choose_shop[main_total] = {'shop': shop,
                                       'total_shop': total_shop,
                                       'main_total': main_total}

        cheapest_store = choose_shop[min(choose_shop)]

        if cheapest_store['main_total'] < client.money:
            date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"{client.name} rides to {cheapest_store['shop'].name}\n")

            print(f"Date: {date_now}")
            print(f"Thanks, {client.name}, for you purchase!")
            print("You have bought: ")

            for product, amount in client.product_cart.items():
                print(f"{amount} {product}s for "
                      f"{cheapest_store['shop'].products[product] * amount}"
                      f" dollars")

            print(f"Total cost is {cheapest_store['total_shop']} dollars")
            print("See you again!\n")
            print(f"{client.name} rides home")
            print(f"{client.name} now has "
                  f"{client.money - cheapest_store['main_total']}"
                  f" dollars\n")

        else:
            print(f"{client.name} doesn't have enough money"
                  f" to make purchase in any shop")


if __name__ == '__main__':
    shop_trip()
