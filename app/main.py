import datetime
from app.shop import Shop
from app.customer import Customer
from app.unpack_json_file import list_of_shops, list_of_customers


def shop_trip() -> None:
    for customer_data in list_of_customers:
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")
        choice_shop = ""
        num = 1000000
        for shops_data in list_of_shops:
            shop = Shop(**shops_data)
            total_cost = (customer.road_cost(shop)
                          + sum(customer.shop_total_cost(shop)))
            if num > total_cost:
                num = total_cost
                choice_shop = shop
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
        if customer.money < num:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            return
        current = datetime.datetime.now()
        print(f"{customer.name} rides to {choice_shop.name}\n\n"
              f"Date: {current.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        index = 0
        price_choice_shop = customer.shop_total_cost(choice_shop)
        for products, count in customer.product_cart.items():
            print(f"{count} {products}s "
                  f"for {price_choice_shop[index]} dollars")
            index += 1
        money = (customer.money
                 - (customer.road_cost(choice_shop)
                    + sum(customer.shop_total_cost(choice_shop))))
        print(f"Total cost is {sum(price_choice_shop)} dollars"
              f"\nSee you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has {money} dollars\n")
