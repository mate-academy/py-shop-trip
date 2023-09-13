import math
import datetime
from app.customer import Customer
from app.shop import Shop
from app.customer import customers_and_content


def shop_trip() -> str:
    customers, content, shops, priсe_fuel = customers_and_content()
    for name_customer in customers:
        name = name_customer.get("name")
        product_cart = name_customer.get("product_cart")
        location = name_customer.get("location")
        money = name_customer.get("money")
        car = name_customer.get("car")
        info_dict = (
            {"name": name,
             "location": location,
             "product_cart": product_cart,
             "money": money}
        )
        customer_instance = Customer(car, info_dict)
        fuel_consumption_car = customer_instance.car
        name = customer_instance.name
        product_cart = customer_instance.product_cart
        distance_customer_x = customer_instance.location[0]
        distance_customer_y = customer_instance.location[1]
        total_price_list = []
        print(f"{name} has {money} dollars")
        for element in shops:
            name_shop = element.get("name")
            location = element.get("location")
            products = element.get("products")
            info_dict = {"location": location, "products": products}
            shop_instance = Shop(info_dict)
            distance_location_shop_x = shop_instance.location[0]
            distance_location_shop_y = shop_instance.location[1]
            product = shop_instance.products
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
            total_price_list.sort()
            total_price_min = total_price_list[0]
            if total_price <= total_price_min:
                total = total_price
                name_cust_min = name_shop
                products_list = product
                total_price_dol = total_price - distance_priсe

        if money >= total:
            print(f"{name} rides to {name_cust_min}\n")
            datetime_form = datetime.datetime.now()
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for items in product:
                print(
                    f"{product_cart[items]} {items}s "
                    f"for {products_list[items] * product_cart[items]} "
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
