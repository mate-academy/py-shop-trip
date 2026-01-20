from decimal import Decimal, ROUND_HALF_UP
import json

from app.customer import Customer
from app.shop import Shop


with open("app/config.json", "r") as json_file:
    data_dict = json.load(json_file)

FUEL_PRICE = Decimal(data_dict["FUEL_PRICE"])

customers = [Customer(*data_dict["customers"][i].values())
             for i in range(len(data_dict["customers"]))]

shops = [Shop(*data_dict["shops"][i].values())
         for i in range(len(data_dict["shops"]))]


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_total_cost = Decimal("Infinity")
        min_shop = None

        for shop in shops:
            fuel_cost = customer.calc_trip_cost(shop, FUEL_PRICE) * 2
            products_price = shop.calc_total_cost(customer.product_cart)
            total_cost = fuel_cost + products_price
            total_cost = total_cost.quantize(Decimal("0.01"),
                                             rounding=ROUND_HALF_UP)

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

            if total_cost <= min_total_cost:
                min_total_cost = total_cost
                min_shop = shop

        if customer.money < min_total_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            break
        print(
            f"{customer.name} rides to {min_shop.name}\n\n"
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )
        for product in customer.product_cart:
            prod_cost = min_shop.product_cost(
                product, customer.product_cart[product]
            )
            print(
                f"{customer.product_cart[product]} {product}s for {prod_cost} "
                f"dollars"
            )
        total_cost = min_shop.calc_total_cost(customer.product_cart)
        print(f"""Total cost is {total_cost} dollars
See you again!\n\n{customer.name} rides home
{customer.name} now has {customer.money - min_total_cost} dollars\n""")
