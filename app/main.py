from app.customer import customers_and_content
from datetime import datetime
from app.car import PriseKm


def shop_trip() -> str:
    customers, content = customers_and_content()
    count_ = 0
    for elements_cust in customers:
        name_cust = elements_cust.get("name")
        product_cart = elements_cust.get("product_cart")
        shops = content.get("shops")
        quantities = product_cart
        total_cost_ = 1000000000000
        money_cost = elements_cust.get("money")
        print(f"{name_cust} has {money_cost} dollars")
        for elements in shops:
            name1 = elements.get("name")
            products = elements.get("products")
            distens_prise_ = PriseKm.distens_prise()[count_]
            total_cost = (
                sum(products[item]
                    * quantities.get(item, 0) for item in products)
                + float(distens_prise_)
            )
            total_cost1 = (
                sum(products[item]
                    * quantities.get(item, 0)
                    for item in products)
            )
            count_ += 1
            print(f"{name_cust}'s trip to the {name1} costs {total_cost}")
            if total_cost < total_cost_:
                total_cost_ = total_cost
                name_coust_min = name1
                products_list = products
                total_cost_dol = total_cost1
            else:
                total_cost_ = total_cost_
        if money_cost - total_cost_ >= 0:
            print(f"{name_cust} rides to {name_coust_min}")
            print()
            datetime_form = datetime(2021, 1, 4, 12, 33, 41)
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                (f"Thanks, {name_cust}, for your purchase!\n"
                 f"You have bought: \n"
                 f"{quantities['milk']} milks for"
                 f" {products_list['milk'] * quantities['milk']} dollars\n"
                 f"{quantities['bread']} breads for"
                 f" {products_list['bread'] * quantities['bread']} dollars\n"
                 f"{quantities['butter']} butters for"
                 f" {products_list['butter'] * quantities['butter']} dollars\n"
                 f"Total cost is {total_cost_dol} dollars\nSee you again!\n\n"
                 f"{name_cust} rides home\n"
                 f"{name_cust} now has {money_cost - total_cost_} dollars\n")
            )
        else:
            print(
                (f"{name_cust} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
