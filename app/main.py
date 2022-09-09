from app.open_json import customers
from app.open_json import shops
from app.car import trip_price
from app.shop import purchase


def shop_trip():

    for i in range(len(customers)):
        index_store = trip_price(customers[i],
                                 shops,
                                 customers[i]["product_cart"]["milk"],
                                 customers[i]["product_cart"]["bread"],
                                 customers[i]["product_cart"]["butter"])
        if index_store is not None:
            purchase(customers[i]["product_cart"]["milk"],
                     customers[i]["product_cart"]["bread"],
                     customers[i]["product_cart"]["butter"],
                     customers[i],
                     index_store[0])
            money_left = customers[i]["money"] - index_store[1]
            print(f'{customers[i]["name"]} now has {money_left} dollars\n')


shop_trip()
