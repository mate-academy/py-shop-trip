import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
    fuel = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]
    customers = []
    for cust in config["customers"]:
        cc = Customer(name=cust["name"], product_cart=cust["product_cart"],
                      location=cust["location"],
                      money=cust["money"],
                      car=Car(**cust["car"]))
        customers.append(cc)
    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")
        affords = []
        for shop in shops:
            price = cust.trip_cost(shop, fuel)
            print(f"{cust.name}'s trip to"
                  f" the {shop.name} costs {round(price, 2)}")
            if price <= cust.money:
                affords.append((price, shop))
        if not affords:
            print(f"{cust.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            continue
        affords.sort()
        x, best = affords[0]
        print(f"{cust.name} rides to {best.name}\n")
        cust.ride_to(best.location)
        best.print_receipt(cust.name, cust.product_cart)
        print(f"{cust.name} rides home")
        cust.ride_home()
        cust.money = cust.money - x
        print(f"{cust.name} now has {round(cust.money, 2)} dollars\n")
