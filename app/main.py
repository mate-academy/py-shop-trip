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

        count_milk = customer.product_cart["milk"]
        count_bread = customer.product_cart["bread"]
        count_butter = customer.product_cart["butter"]
        milk_value = count_milk * shop_cheapest_check.products["milk"]
        bread_value = count_bread * shop_cheapest_check.products["bread"]
        butter_value = count_butter * shop_cheapest_check.products["butter"]

        total_value = milk_value + bread_value + butter_value

        print("You have bought: ")
        print(f"{count_milk} milks for {milk_value} dollars")
        print(f"{count_bread} breads for {bread_value} dollars")
        print(f"{count_butter} butters for {butter_value} dollars")
        print(f"Total cost is {total_value} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{customer.money - min_price_trip} dollars"
        )
        print()
