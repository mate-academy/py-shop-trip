import math
import datetime
from app.customer import customers_and_content


def shop_trip() -> str:
    content = customers_and_content()
    shops = content.get("shops")
    customers = content.get("customers")
    priсe_fuel = content.get("FUEL_PRICE")
    for name__ in customers:
        fuel_consumption_car = (
            name__.get("car").get("fuel_consumption")
        )
        location_customer = name__.get("location")
        distance_custom_x = location_customer[0]
        distance_custom_y = location_customer[1]
        quantities = name__.get("product_cart")
        money = name__.get("money")
        product = name__.get("product_cart")
        name = name__.get("name")
        total_cust_list = []
        print(f"{name} has {money} dollars")
        for element in shops:
            name_ = element.get("name")
            location = element.get("location")
            product = element.get("products")
            coordinates_shop = location
            distance_location_shop_x = coordinates_shop[0]
            distance_location_shop_y = coordinates_shop[1]
            distance = (
                math.sqrt((distance_custom_x
                           - distance_location_shop_x) ** 2
                          + (distance_custom_y
                             - distance_location_shop_y) ** 2)
            )
            priсe_distance = (
                (distance * 2 / 100)
                * fuel_consumption_car
                * priсe_fuel
            )
            distance_priсe = round(priсe_distance, 2)
            total_cust = (
                sum(product[item]
                    * quantities.get(item, 0)
                    for item in product)
                + float(distance_priсe)
            )
            print(
                f"{name}'s trip to the "
                f"{name_} costs "
                f"{total_cust}"
            )
            total_cust_list.append(total_cust)
            total_cust_list.sort()
            total_cust_ = total_cust_list[0]
            if total_cust <= total_cust_:
                total = total_cust
                name_cust_min = name_
                products_list = product
                total_cust_dol = total_cust - distance_priсe

        if money - total >= 0:
            print(f"{name} rides to {name_cust_min}\n")
            datetime_form = datetime.datetime.now()
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for product_ in product:
                print(
                    f"{quantities[product_]} {product_}s "
                    f"for {products_list[product_] * quantities[product_]} "
                    f"dollars"
                )
            print(
                f"Total cost is {round(total_cust_dol, 2)} dollars\n"
                f"See you again!\n\n"
                f"{name} rides home\n"
                f"{name} now has {money - total} dollars\n"
            )
        else:
            print(
                (f"{name} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
