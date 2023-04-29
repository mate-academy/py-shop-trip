from app.customer import customers_list
from app.shop import shop_list


def shop_trip() -> None:
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        shop_cheapest_check = shop_list[0]
        min_price_trip = customer.price_trip(shop_list[0])
        for shop in shop_list:
            price_trip = customer.price_trip(shop)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {price_trip}")
            if min_price_trip > price_trip:
                min_price_trip = price_trip
                shop_cheapest_check = shop

        if customer.money <= min_price_trip:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {shop_cheapest_check.name}")
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")

        print("You have bought: ")

        for product_name in customer.product_cart.keys():
            product_count = customer.product_cart[product_name]
            product_value = product_count * (
                shop_cheapest_check.products[product_name]
            )
            print(f"{product_count} {product_name}s "
                  f"for {product_value} dollars")

        print(f"Total cost is "
              f"{customer.product_value(shop_cheapest_check)} "
              f"dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{customer.money - min_price_trip} dollars"
        )
        print()
