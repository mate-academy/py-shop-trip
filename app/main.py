import datetime

from app.create_variales import create_customers_examples
from app.create_variales import create_fuel_cost
from app.create_variales import create_shops_examples


def shop_trip() -> None:
    shops = create_shops_examples()
    fuel_cost = create_fuel_cost()
    customers = create_customers_examples()
    for customer in customers:
        calculate_min_result = []
        print(f"{customer.name} has {customer.money} dollars")
        dict_for_calculate_shop = {}
        for shop in shops:
            result = 0
            milk_cost = shop.milk * customer.milk
            bread_cost = shop.bread * customer.bread
            butter_cost = shop.butter * customer.butter
            result += (milk_cost + bread_cost + butter_cost)
            delta_x_2 = (customer.location[0] - shop.location[0]) ** 2
            delta_y = (customer.location[1] - shop.location[1]) ** 2
            path_len = (delta_x_2 + delta_y) ** 0.5
            tot_run = fuel_cost * customer.fuel_consumption
            trip_cost = (tot_run * path_len * 2 / 100)
            calculate_min_result.append(round(trip_cost, 2) + result)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {(result + round(trip_cost, 2)):.2f}")
            dict_for_calculate_shop[shop.name] = round(trip_cost, 2) + result
        min_value = min(calculate_min_result)
        cheapest_shop = \
            [key for key, value in dict_for_calculate_shop.items()
             if value == min_value][0]
        cheapest_shop_name = [shop for shop in shops
                              if shop.name == cheapest_shop][0]
        if customer.money < min_value:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_shop}\n")
            customer.location = cheapest_shop_name.location
            now = datetime.datetime.now()
            print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            milk_cost = round(customer.milk * cheapest_shop_name.milk, 2)
            bread_cost = round(customer.bread * cheapest_shop_name.bread, 2)
            butter_cost = round(customer.butter * cheapest_shop_name.butter, 2)
            print(f"{customer.milk} milks for {milk_cost:g} dollars")
            print(f"{customer.bread} breads for {bread_cost:g} dollars")
            print(f"{customer.butter} butters for {butter_cost:g} dollars")
            print(f"Total cost is "
                  f"{butter_cost + bread_cost + milk_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{(customer.money - min_value):.2f} dollars\n")
