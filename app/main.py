from datetime import datetime
from app.car import PriсeKm
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> str:
    (
        location_customer1,
        fuel_consumption_car3,
        priсe_fuel,
        product_cart3,
        money_custom,
        name_customer
    ) = Customer.customer_location()
    count_ = 0
    for name_cust in name_customer:
        quantities = product_cart3.get(name_cust)
        total_cust_ = 1000000000000
        money_cust = money_custom.get(name_cust)
        print(f"{name_cust} has {money_cust} dollars")
        location_shop, name_shop, product_shop = Shop.shop_location_shop()
        for name_shop_element in name_shop:
            products_shop1 = product_shop.get(name_shop_element)
            distance_priсe_ = PriсeKm.distance_priсe()[count_]
            total_cust = (
                sum(products_shop1[item]
                    * quantities.get(item, 0) for item in products_shop1)
                + float(distance_priсe_)
            )
            total_cust1 = (
                sum(products_shop1[item]
                    * quantities.get(item, 0)
                    for item in products_shop1)
            )
            count_ += 1
            print(
                f"{name_cust}'s trip to the "
                f"{name_shop_element} costs "
                f"{total_cust}"
            )
            if total_cust < total_cust_:
                total_cust_ = total_cust
                name_cust_min = name_shop_element
                products_list = products_shop1
                total_cust_dol = total_cust1
            else:
                total_cust_ = total_cust_
        if money_cust - total_cust_ >= 0:
            print(f"{name_cust} rides to {name_cust_min}\n")
            datetime_form = datetime(2021, 1, 4, 12, 33, 41)
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name_cust}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for product in products_shop1:
                print(
                    f"{quantities[product]} {product}s "
                    f"for {products_list[product] * quantities[product]} "
                    f"dollars"
                )
            print(
                f"Total cost is {total_cust_dol} dollars\n"
                f"See you again!\n\n"
                f"{name_cust} rides home\n"
                f"{name_cust} now has {money_cust - total_cust_} dollars\n"
            )
        else:
            print(
                (f"{name_cust} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
