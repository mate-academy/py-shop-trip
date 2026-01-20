import json
from app.Classes.customer import Customer
from app.Classes.shop import Shop
from app.Classes.shop import trip_cost
from app.Classes.shop import customer_service


def shop_trip() -> None:
    with (open("app/config.json", "r")
          as config):
        data = json.load(config)
        customers_info = data["customers"]
        shops_info = data["shops"]
        customer_list = [
            (Customer(info["name"],
                      info["product_cart"],
                      info["location"],
                      info["money"],
                      info["car"]
                      )) for info in customers_info]
        shop_list = [
            Shop(info["name"],
                 info["location"],
                 info["products"])
            for info in shops_info]
        for customer in customer_list:
            print(f"{customer.name} has {customer.money} dollars")
            total_cost = {}
            for shop in shop_list:
                total_cost[shop.name] = trip_cost(customer, shop)
                print(f"{customer.name}'s trip "
                      f"to the {shop.name} costs "
                      f"{round(trip_cost(customer, shop), 2)}")
            minimal_price_shop = min(total_cost, key=total_cost.get)
            target_shop = None
            for shop in shop_list:
                if shop.name == minimal_price_shop:
                    target_shop = shop
                    break
            if customer.money > total_cost[minimal_price_shop]:
                print(f"{customer.name} rides to {minimal_price_shop}")
                print("")
                customer_service(customer, target_shop)
                print(f"{customer.name} rides home")
                money_left = customer.money - (
                    round(trip_cost(customer, target_shop), 2)
                )
                print(f"{customer.name} now has {money_left} dollars")
                print("")
            else:
                print(f"{customer.name} doesn't have enough money"
                      f" to make a purchase in any shop")
