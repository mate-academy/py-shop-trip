import datetime
from math import sqrt

from app.fuel import fuel_price
from app.customers import customers_list
from app.shops import shops_list


def shop_trip() -> None:
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")

        selected_trip_cost = None
        for shop in shops_list:
            distance = sqrt(
                pow(abs(customer.location[0] - shop.location[0]), 2)
                + pow(abs(customer.location[1] - shop.location[1]), 2)
            )
            products_cost = sum(num * shop.products[prod] for prod, num
                                in customer.product_cart.items())
            trip_cost = round(customer.car_fuel_consumption * fuel_price
                              * distance * 2) / 100 + products_cost
            if trip_cost == int(trip_cost):
                cost = f"{int(trip_cost)}"
            else:
                cost = f"{trip_cost: .2f}"
            print(f"{customer.name}'s trip to the {shop.name} costs{cost}")

            if not selected_trip_cost or trip_cost < selected_trip_cost:
                selected_shop = shop
                selected_trip_cost = trip_cost
                if products_cost == int(products_cost):
                    selected_products_cost = int(products_cost)
                else:
                    selected_products_cost = products_cost

        if selected_trip_cost > customer.money:
            print(f"{customer.name} doesn't have enough money to make "
                  f"a purchase in any shop")
            continue

        print(f"{customer.name} rides to {selected_shop.name}")
        print()
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, amount in customer.product_cart.items():
            product_str = f"{product}" if amount == 1 else f"{product}s"
            price = selected_shop.products[product] * amount
            price = int(price) if price == int(price) else price
            print(f"{amount} {product_str} for {price} dollars")

        print(f"Total cost is {selected_products_cost} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has"
              f"{customer.money - selected_trip_cost: .2f} dollars")
        print()
