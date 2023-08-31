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
        money_costum,
        name_custom
    ) = Customer.customer_location()
    count_ = 0
    for number in location_customer1:
        name_cust = name_custom.get(number)
        quantities = product_cart3.get(number)
        total_cost_ = 1000000000000
        money_cost = money_costum.get(number)
        print(f"{name_cust} has {money_cost} dollars")
        location_shop, name_shop, product_shop = Shop.shop_location_shop()
        for elements in location_shop:
            name_shop1 = name_shop.get(elements)
            products_shop1 = product_shop.get(elements)
            distance_priсe_ = PriсeKm.distance_priсe()[count_]
            total_cost = (
                sum(products_shop1[item]
                    * quantities.get(item, 0) for item in products_shop1)
                + float(distance_priсe_)
            )
            total_cost1 = (
                sum(products_shop1[item]
                    * quantities.get(item, 0)
                    for item in products_shop1)
            )
            count_ += 1
            print(f"{name_cust}'s trip to the {name_shop1} costs {total_cost}")
            if total_cost < total_cost_:
                total_cost_ = total_cost
                name_coust_min = name_shop1
                products_list = products_shop1
                total_cost_dol = total_cost1
            else:
                total_cost_ = total_cost_
        if money_cost - total_cost_ >= 0:
            print(f"{name_cust} rides to {name_coust_min}\n")
            datetime_form = datetime(2021, 1, 4, 12, 33, 41)
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name_cust}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for produc in products_shop1:
                print(
                    f"{quantities[produc]} {produc}s "
                    f"for {products_list[produc] * quantities[produc]} dollars"
                )
            print(
                f"Total cost is {total_cost_dol} dollars\n"
                f"See you again!\n\n"
                f"{name_cust} rides home\n"
                f"{name_cust} now has {money_cost - total_cost_} dollars\n"
            )
        else:
            print(
                (f"{name_cust} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
