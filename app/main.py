import json
from app.shop import Shop
from app.customer import Customer
from app.trip_price_count import count_trip_distance, \
    goods_price_counting, \
    shop_bill


def shop_trip() -> None:
    with open("app/config.json", "r") as data_file:
        data = json.load(data_file)
        list_of_shops = []
        list_of_customers = []
        fuel_price = data.get("FUEL_PRICE")
        for shops in data.get("shops"):
            list_of_shops.append(Shop(shops.get("name"),
                                      shops.get("location"),
                                      shops.get("products")))
        for client in data.get("customers"):
            list_of_customers.append(
                Customer(client.get("name"),
                         client.get("product_cart"),
                         client.get("location"),
                         client.get("money"),
                         client.get("car").get("brand"),
                         client.get("car").get("fuel_consumption"))
            )
        for get_client in list_of_customers:
            print(f"{get_client.name} has {get_client.money} dollars")
            low_price = {}
            for trip_shop in list_of_shops:
                price_distance = count_trip_distance(get_client,
                                                     trip_shop,
                                                     fuel_price)
                price_goods = goods_price_counting(get_client, trip_shop)
                total_price = price_distance + price_goods
                low_price.update({trip_shop.store: total_price})
                print(f"{get_client.name}'s "
                      f"trip to the {trip_shop.store} costs {total_price}")
            chip_store = min(low_price.values())
            best_price = [key for key,
                          value in low_price.items() if value == chip_store
                          ]
            if chip_store <= get_client.money:
                print(f"{get_client.name} rides to {best_price[0]}\n")
                shop_bill(get_client,
                          best_price[0],
                          list_of_shops)
                rest_of_money = get_client.money - chip_store
                print(f"{get_client.name} now has {rest_of_money} dollars\n")
            else:
                print(f"{get_client.name} doesn't "
                      f"have enough money to make purchase in any shop")
