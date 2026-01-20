import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    # write your code here
    with open("app/config.json", "r") as k:
        data = json.load(k)
        for client in data["customers"]:
            shop_dict = {}
            customer = Customer(client, data["FUEL_PRICE"])
            print(f"{customer.name} has {customer.money} dollars")
            reserve_dict = {}
            count = 0
            for market in data["shops"]:
                shop = Shop(market)
                shop_dict.update({shop.name: shop.price_products(customer)})
                if customer.money < shop.cost:
                    count += 1
                reserve_dict.update({shop.name: [shop.dict_products,
                                                 shop.location,
                                                 shop.distance,
                                                 shop.time]})
            if count == len(data["shops"]):
                print(f"{customer.name} doesn't have enough "
                      f"money to make a purchase in any shop")
                continue
            bargain_shop = min(shop_dict, key=shop_dict.get)
            print(f"{customer.name} rides to {bargain_shop}\n")
            home = customer.location
            customer.location = reserve_dict[bargain_shop][1]
            print(f"Date: {reserve_dict[bargain_shop][3]}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, price in reserve_dict[bargain_shop][0].items():
                if price[0] % int(price[0]) == 0:
                    print(f"{price[1]} {product}s for {int(price[0])} dollars")
                else:
                    print(f"{price[1]} {product}s for {price[0]} dollars")
            cost_bargain_shop = shop_dict[bargain_shop]
            total_cost = cost_bargain_shop - reserve_dict[bargain_shop][2]
            print(f"Total cost is {round(total_cost, 2)} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home
            print(f"{customer.name} now has "
                  f"{customer.money - cost_bargain_shop} dollars\n")
