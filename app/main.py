from app.car import Car
from app.shop import Shop
from app.customer import Customer
import json


def shop_trip() -> None:
    with open("app/config.json") as open_file:
        data = json.load(open_file)
    customers = data["customers"]
    customers_list = []
    fuel_price = data["FUEL_PRICE"]
    for customer in customers:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        new_customer = Customer(customer["name"],
                                customer["product_cart"],
                                customer["location"],
                                customer["money"],
                                car)
        customers_list.append(new_customer)

    shops_list = []
    shops = data["shops"]
    for shop in shops:
        new_shop = Shop(shop["name"], shop["location"], shop["products"])
        shops_list.append(new_shop)

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        can_afford = False
        for shop in shops_list:
            trip_cost = customer.road_to_shop(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {trip_cost:.2f}")
            if trip_cost <= customer.money:
                can_afford = True
        if not can_afford:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            continue
        chosen_shop = customer.choose_shop(shops_list, fuel_price)
        print(f"{customer.name} rides to {chosen_shop.name}")
        # date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        total_cost = 0
        for item, quantity in customer.product_cart.items():
            item_cost = chosen_shop.products[item] * quantity
            if isinstance(item_cost, float):
                item_cost = round(item_cost, 1)

            print(f"{quantity} {item}s for {item_cost} dollars")
            total_cost += item_cost
        print(f"Total cost is {total_cost:.1f} dollars")
        print("See you again!")
        customer.money -= customer.road_to_shop(chosen_shop, fuel_price)
        print(f"\n{customer.name} rides home")

        print(f"{customer.name} now has {customer.money:.2f} dollars\n")
