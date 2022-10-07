import json
from datetime import datetime
from app.car import fuel_calculation
from app.costumer import Customer
from app.shop import Shop


def shop_trip():
    with open("app/config.json") as file:
        config = json.load(file)

    # unpacking json
    fuel_price = config.get("FUEL_PRICE")
    customers = config.get("customers")
    shops = config.get("shops")

    # customers list creation
    customers_list = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            location=customer["location"],
            money=customer["money"],
            fuel_consumption=customer["car"]["fuel_consumption"],
            product_cart=customer["product_cart"]
        )
        customers_list.append(customer_instance)

    # shop list creation
    shop_list = []
    for shop in shops:
        shop_instance = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        shop_list.append(shop_instance)

    # spending calculation
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        spends_dict = {}
        spends_dict_invert = {}
        for shop in shop_list:

            # fuel spends calculation
            one_way_fuel_waste = fuel_calculation(
                fuel_price=fuel_price,
                fuel_consumption=customer.fuel_consumption,
                shop_location=shop.location,
                customer_location=customer.location
            )

            # trip spends calculation
            trip_spends = 0
            shop_spends = 0
            bill_content = ""  # content for a bill
            for product in customer.product_cart:
                product_spends = 0
                product_spends += \
                    customer.product_cart[product] * shop.products[product]
                shop_spends += product_spends
                bill_content += f"{customer.product_cart[product]}" \
                                f" {product}s for {product_spends} dollars\n"
            trip_spends += round(shop_spends + one_way_fuel_waste * 2, 2)
            spends_dict[shop.name] = trip_spends, shop_spends\
                , one_way_fuel_waste, bill_content
            spends_dict_invert[trip_spends] = shop.name
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs", trip_spends)
        cheapest_trip_shop = spends_dict_invert[min(spends_dict_invert)]

        # add data about best shop in customer instance
        customer.best_shop["trip_spends"] = spends_dict[cheapest_trip_shop][0]
        customer.best_shop["shop_spends"] = spends_dict[cheapest_trip_shop][1]
        customer.best_shop["one_way_fuel_waste"] \
            = spends_dict[cheapest_trip_shop][2]
        customer.best_shop["bill_content"] = spends_dict[cheapest_trip_shop][3]

        # customer rides to the shop
        if customer.money < customer.best_shop["trip_spends"]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            date = datetime(2021, 1, 4, 12, 33, 41, 51204)
            money_left = customer.money - customer.best_shop['trip_spends']
            print(f"{customer.name} rides to {cheapest_trip_shop}\n")
            print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}\n"
                  f"Thanks, {customer.name}, for you purchase!\n"
                  f"You have bought: \n"
                  f"{customer.best_shop['bill_content']}"
                  f"Total cost is {customer.best_shop['shop_spends']}"
                  f" dollars\n"
                  f"See you again!\n\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has {round(money_left, 2)} dollars\n")
