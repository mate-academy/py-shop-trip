import math
import datetime
from app.customer import Customer
from app.customer import customers_and_content


def shop_trip() -> str:
    customers, shops, priсe_fuel = customers_and_content()
    for customer in customers:
        car = customer.get("car")
        customer_instance = Customer(car, customer)
        fuel_consumption_car = customer_instance.car
        money = customer.get("money")
        name = customer.get("name")
        product_cart = customer.get("product_cart")
        distance_customer_x = customer.get("location")[0]
        distance_customer_y = customer.get("location")[1]
        total_price_list = []
        print(f"{name} has {money} dollars")
        for shop in shops:
            name_shop = shop.get("name")
            distance_location_shop_x = shop.get("location")[0]
            distance_location_shop_y = shop.get("location")[1]
            product = shop.get("products")
            distance = (
                math.sqrt((distance_customer_x
                           - distance_location_shop_x) ** 2
                          + (distance_customer_y
                             - distance_location_shop_y) ** 2)
            )
            priсe_distance = (
                (distance * 2 / 100)
                * fuel_consumption_car.fuel_consumption
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
            total_price_list.append(total_price)
            if total_price <= min(total_price_list):
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
