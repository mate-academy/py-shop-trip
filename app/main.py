import json
from app.classes import Customer, Car, Shop
from app.helpfuncs import shopping_cost, trip_cost, shopping_start


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        json_info = json.load(config)
        customers = json_info["customers"]
        shops = json_info["shops"]
        fuel_price = json_info["FUEL_PRICE"]
    for customer in customers:
        shopper = Customer.create_class(customer)
        car = Car.create_class(shopper.car)
        print(f"{shopper.name} has {shopper.money} dollars")
        expense = 0
        best_shop = ""
        prod_pack = {}
        for shop in shops:
            destination = Shop.create_class(shop)
            trip = trip_cost(
                shopper.location,
                destination.location,
                fuel_price,
                car.fuel_consumption
            )
            shopping, pack = shopping_cost(
                shopper.product_cart,
                destination.products
            )
            total = trip + shopping
            if expense == 0 or total < expense:
                expense = total
                best_shop = destination.name
                prod_pack = pack
                receipt = shopping
            print(f"{shopper.name}'s trip"
                  f" to the {destination.name} costs {total}")
        shopping_start(
            shopper.name,
            shopper.money,
            receipt,
            expense,
            best_shop,
            prod_pack
        )
