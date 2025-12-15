import json
from app.shop import Shop
from app.car import Car
from app.customer import Customer


def shop_trip() -> None:
    with (open("app/config.json", "r")
          as file_json):
        data = json.load(file_json)
    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"],
                          Car(customer["car"]["brand"],
                              customer["car"]["fuel_consumption"],
                              customer["location"],
                              )
                          )
                 for customer
                 in data["customers"]
                 ]
    shops = [Shop(shop["name"],
                  shop["location"],
                  shop["products"], )
             for shop
             in data["shops"]
             ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        road_shop = []
        for shop in shops:
            full_price = round(customer.car.price_trip(shop.location,
                                                       fuel_price)
                               + shop.purchase_price(customer)
                               + customer.car.price_trip(customer.location_h,
                                                         fuel_price), 2)
            if road_shop:
                if road_shop[0] > full_price:
                    road_shop = [full_price, shop]
            else:
                road_shop = [full_price, shop]
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {full_price}")
        if road_shop[0] <= customer.money:
            print(f"{customer.name} rides to {road_shop[1].name}\n")
            now = "04/01/2021 12:33:41"
            customer.buy(road_shop[0])
            print(f"Date: {now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product in customer.product_cart:
                if product in road_shop[1].products:
                    prt1 = (road_shop[1].products[product]
                            * customer.product_cart[product])
                    prt = (int(road_shop[1].products[product]
                               * customer.product_cart[product])
                           if road_shop[1].products[product]
                           * customer.product_cart[product]
                           == int(road_shop[1].products[product]
                                  * customer.product_cart[product])
                           else prt1)
                    print(
                        f"{customer.product_cart[product]} {product}s for "
                        f"{prt} "
                        f"dollars")
            print(f"Total cost is {road_shop[1].purchase_price(customer)} "
                  f"dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)} "
                  f"dollars")
            print()
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")


shop_trip()
