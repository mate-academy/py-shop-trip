import json
from app.customer import Customer
from app.car import car_cost
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)
        shops = info["shops"]
        customers = info["customers"]
        fuel_price = info["FUEL_PRICE"]
        list_of_shops = []

        for shop in shops:
            shop = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            list_of_shops.append(shop)

        for data in customers:
            shop_dict = {}
            customer = Customer(
                name=data["name"],
                product_cart=data["product_cart"],
                location=data["location"],
                money=data["money"],
                car=data["car"])

            print(customer.__str__())

            for shop in list_of_shops:
                products_cost = shop.cost_of_products(customer)
                car = car_cost(customer, shop, fuel_price)
                trip_cost = round((car + products_cost), 2)
                shop_dict[trip_cost] = shop
                print(f"{customer.name}'s trip to the {shop.name} "
                      f"costs {trip_cost}")
            min_trip_cost = min(shop_dict.keys())
            suitable_shop = shop_dict[min_trip_cost]
            if customer.money <= min_trip_cost:
                print(f"{customer.name} doesn't have enough "
                      f"money to make purchase in any shop")
            else:
                customer.shopping(suitable_shop.name, min_trip_cost)
                suitable_shop.purchase_receipt(customer)
                customer.get_home()
