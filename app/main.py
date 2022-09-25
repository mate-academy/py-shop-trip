import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip():
    with open("config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        custom_list = [Customer(customer_) for customer_ in data["customers"]]
        shop_list = [Shop(shop_) for shop_ in data["shops"]]
        for customer in custom_list:
            print(f"{customer.name} has {customer.money} dollars")
            choice_list = dict()
            flag = False
            for shop in shop_list:
                cost_product = shop.cost(customer.product_cart)
                if cost_product is not None:
                    car = Car(customer.car)
                    sub_x = customer.location[0] - shop.location[0]
                    sub_y = customer.location[1] - shop.location[1]
                    distance = (sub_x ** 2 + sub_y ** 2) ** 0.5
                    cost_trip = car.cost_trip(distance, fuel_price)
                    sum_cost = round(cost_product + cost_trip * 2, 2)
                    choice_list[shop.name] = (
                        customer.name, customer.money, sum_cost, shop)
                    if customer.money > cost_product:
                        flag = True
                    print(f"{customer.name}'s trip to the {shop.name} "
                          f"costs {sum_cost}")
            if flag:
                cost_min = 0
                for choice_elm in choice_list:
                    if cost_min == 0:
                        cost_min = choice_list[choice_elm][2]
                        choice_shop = choice_list[choice_elm]
                        sum_cost = choice_list[choice_elm][2]
                    elif cost_min > choice_list[choice_elm][2]:
                        cost_min = choice_list[choice_elm][2]
                        choice_shop = choice_list[choice_elm]
                        sum_cost = choice_list[choice_elm][2]
                print(f"{customer.name} rides to {choice_shop[3].name}\n")
                choice_shop[3].print_cash_receipt(
                    customer.name, customer.product_cart)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now "
                      f"has {customer.money - sum_cost} dollars\n")
            else:
                print(f"{customer.name} doesn't have enough money "
                      f"to make purchase in any shop")
