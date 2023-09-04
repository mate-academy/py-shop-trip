from datetime import datetime
from app.car import PriсeKm
from app.customer import Customer
from app.shop import Shop
from app.customer import customers_and_content


def shop_trip() -> str:
    (
        location_customer,
        fuel_consumption_car,
        priсe_fuel,
        product_cart,
        money_custom,
        name_customer
    ) = Customer.customer_location()
    count_ = 0
    for name_cust in name_customer:
        quantities = product_cart.get(name_cust)
        total_cust_list = []
        money_cust = money_custom.get(name_cust)
        print(f"{name_cust} has {money_cust} dollars")
        customers, content = customers_and_content()
        shops = content.get("shops")
        for element in shops:
            name_shop_element = element.get("name")
            location_shop_ = element.get("location")
            product_shop_ = element.get("products")
            products_shop_ = element.get("products")
            shop = Shop(
                element,
                name_shop_element,
                location_shop_,
                product_shop_
            )
            distance_priсe_ = PriсeKm.distance_priсe()[count_]
            total_cust = (
                sum(products_shop_[item]
                    * quantities.get(item, 0) for item in products_shop_)
                + float(distance_priсe_)
            )
            total_cust___ = (
                sum(products_shop_[item]
                    * quantities.get(item, 0)
                    for item in products_shop_)
            )
            count_ += 1
            print(
                f"{name_cust}'s trip to the "
                f"{shop.name_shop_element} costs "
                f"{total_cust}"
            )
            total_cust_list.append(total_cust)
            total_cust_list.sort()
            total_cust_ = total_cust_list[0]
            if total_cust <= total_cust_:
                total_cust_ = total_cust
                name_cust_min = name_shop_element
                products_list = products_shop_
                total_cust_dol = total_cust___

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
            for product in products_shop_:
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
