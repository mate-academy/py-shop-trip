import math
import datetime
from app.shop import Shop
from app.customer import Customer
from app.customer import components_file


def shop_trip() -> None:
    customers, shops, priсe_fuel = components_file()
    customers_list = [Customer(**customer_data) for customer_data in customers]
    for customer in customers_list:
        product_cart = customer.product_cart
        name = customer.name
        money = customer.money
        fuel_consumption_car = customer.car.fuel_consumption
        distance_customer_x, distance_customer_y = customer.location
        total_prices = []
        print(f"{name} has {money} dollars")
        shop_list = [Shop(**shop_data) for shop_data in shops]
        for shop in shop_list:
            name_shop = shop.name
            distance_location_shop_x, distance_location_shop_y = shop.location
            product = shop.products
            distance = (
                math.sqrt((distance_customer_x
                           - distance_location_shop_x) ** 2
                          + (distance_customer_y
                             - distance_location_shop_y) ** 2)
            )
            priсe_distance = (
                (distance * 2 / 100)
                * fuel_consumption_car
                * priсe_fuel
            )
            distance_priсe = round(priсe_distance, 2)

            total_price = (
                sum(
                    price * product_cart.get(product, 0)
                    for product, price in product.items()
                )
                + float(distance_priсe)
            )
            print(
                f"{name}'s trip to the "
                f"{name_shop} costs "
                f"{total_price}"
            )
            total_prices.append(total_price)
            if total_price <= min(total_prices):
                total = total_price
                cust_min = name_shop
                products_list = product
                total_price_dol = total_price - distance_priсe

        if money >= total:
            print(f"{name} rides to {cust_min}\n")
            datetime_form = datetime.datetime.now()
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for items in product:
                price = products_list[items] * product_cart[items]
                print(
                    f"{product_cart[items]} {items}s "
                    f"for {str(str(price).rstrip('0')).rstrip('.')} "
                    f"dollars"
                )
            print(
                f"Total cost is {round(total_price_dol, 2)} dollars\n"
                f"See you again!\n\n"
                f"{name} rides home\n"
                f"{name} now has {money - total} dollars\n"
            )
        else:
            print(
                (f"{name} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
