import datetime
from app.car import PriсeKm
from app.customer import Customer
from app.shop import Shop
from app.customer import customers_and_content


def shop_trip() -> str:
    customers, content = customers_and_content()
    count_ = 0
    shops = content.get("shops")
    shop_instances = []
    for element in shops:
        name = element.get("name")
        location = element.get("location")
        product = element.get("products")
        shop_instance = Shop(
            name,
            location,
            product
        )
        shop_instances.append(shop_instance)
    customers = content.get("customers")
    customer_instances = []
    for name in customers:
        quantities = name.get("product_cart")
        money = name.get("money")
        product = name.get("product_cart")
        priсe_fuel = content.get("FUEL_PRICE")
        fuel_consumption_car = name.get("car").get("fuel_consumption")
        location = name.get("location")
        name = name.get("name")
        customer_instance = Customer(
            location,
            fuel_consumption_car,
            priсe_fuel,
            product,
            money,
            name
        )
        customer_instances.append(customer_instance)
        total_cust_list = []
        print(f"{name} has {money} dollars")
        for shop_instance in shop_instances:
            distance_priсe_ = PriсeKm.distance_priсe()[count_]
            total_cust = (
                sum(shop_instance.product[item]
                    * quantities.get(item, 0)
                    for item in shop_instance.product)
                + float(distance_priсe_)
            )
            total_cust___ = (
                sum(shop_instance.product[item]
                    * quantities.get(item, 0)
                    for item in shop_instance.product)
            )
            count_ += 1
            print(
                f"{name}'s trip to the "
                f"{shop_instance.name} costs "
                f"{total_cust}"
            )
            total_cust_list.append(total_cust)
            total_cust_list.sort()
            total_cust_ = total_cust_list[0]
            if total_cust <= total_cust_:
                total = total_cust
                name_cust_min = shop_instance.name
                products_list = shop_instance.product
                total_cust_dol = total_cust___

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
                f"Total cost is {total_cust_dol} dollars\n"
                f"See you again!\n\n"
                f"{name} rides home\n"
                f"{name} now has {money - total} dollars\n"
            )
        else:
            print(
                (f"{name} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
