import math
import datetime
from app.customer import customers_and_content


def shop_trip() -> str:
    content = customers_and_content()
    shops = content.get("shops")
    customers = content.get("customers")
    priсe_fuel = content.get("FUEL_PRICE")
    for name_customer in customers:
        fuel_consumption_car = (
            name_customer.get("car").get("fuel_consumption")
        )
        location_customer = name_customer.get("location")
        distance_customer_x = location_customer[0]
        distance_customer_y = location_customer[1]
        quantities = name_customer.get("product_cart")
        money = name_customer.get("money")
        product = name_customer.get("product_cart")
        name = name_customer.get("name")
        total_price_list = []
        print(f"{name} has {money} dollars")
        for element in shops:
            name_shop = element.get("name")
            location = element.get("location")
            product = element.get("products")
            coordinates_shop = location
            distance_location_shop_x = coordinates_shop[0]
            distance_location_shop_y = coordinates_shop[1]
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
                sum(product[items]
                    * quantities.get(items, 0)
                    for items in product)
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
                    f"{quantities[items]} {items}s "
                    f"for {products_list[items] * quantities[items]} "
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
