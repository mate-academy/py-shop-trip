import datetime

from app.customer import customers_dicts
from app.shop import shop_dicts, shop_product_carts
from app.car import customers_cars, navigator, fuel_price


def shop_trip() -> None:
    for customer_id, customer in customers_dicts.items():
        chipest_trip = [0, 0, 1000]

        print(f"{customer['name']} has {customer['money']} dollars")

        for shop, shop_products in shop_product_carts.items():
            backet = 0
            for product, number in customer["product_cart"].items():
                backet += shop_products[product] * number

            fuel_loss = customers_cars[customer_id]["fuel_consumption"]
            distance = navigator(customer_id, shop)
            trip_cost = (distance * fuel_loss / 100 * fuel_price) * 2 + backet

            print(f"{customer['name']}'s trip to the "
                  f"{shop_dicts[shop]['name']} costs "
                  f"{round(trip_cost, 2)}")

            if trip_cost < chipest_trip[2]:
                chipest_trip[0] = customer_id
                chipest_trip[1] = shop
                chipest_trip[2] = trip_cost

        if customer["money"] < chipest_trip[2]:
            print(f"{customer['name']} doesn't have "
                  f"enough money to make a purchase "
                  f"in any shop")
        else:
            shop_id = chipest_trip[1]
            print(f"{customer['name']} rides to "
                  f"{shop_dicts[shop_id]['name']}\n")

            now = datetime.datetime.now()
            print(now.strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer['name']}, for your purchase!")
            print("You have bought:")

            total = 0
            for product, number in customer["product_cart"].items():
                price_per_unit = shop_product_carts[shop_id][product]
                product_total = price_per_unit * number
                total += product_total

                display_price = int(product_total) \
                    if product_total == int(product_total) \
                    else product_total

                print(f"{number} {product}s for {display_price} dollars")

            print(f"Total cost is {total} dollars")
            print("See you again!\n")
            print(f"{customer['name']} rides home")

            remaining = round(customer["money"] - chipest_trip[2], 2)
            print(f"{customer['name']} now has {remaining} dollars\n")
