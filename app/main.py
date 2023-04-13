import datetime
from app.shop import Shop
from app.customer import Customer
from app.unpack_json_file import unpack


def shop_trip() -> None:
    shops_data = unpack("app/config.json", "shops")
    shops = [Shop(**data) for data in shops_data]
    for customer_data in unpack("app/config.json", "customers"):
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")
        choice_shop = ""
        num = None
        for shop in shops:
            total_cost = (customer.road_cost(shop)
                          + customer.shop_total_cost(shop))
            if num is None or num > total_cost:
                num = total_cost
                choice_shop = shop
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
        if customer.money < num:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            return
        current = datetime.datetime.now()
        total_cost_choice_shop = customer.shop_total_cost(choice_shop)
        print(f"{customer.name} rides to {choice_shop.name}\n\n"
              f"Date: {current.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        for product, count in customer.product_cart.items():
            print(f"{count} {product}s "
                  f"for {count * choice_shop.products[product]} dollars")
        money = (customer.money
                 - (customer.road_cost(choice_shop)
                    + total_cost_choice_shop))
        print(f"Total cost is {total_cost_choice_shop} dollars"
              f"\nSee you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has {money} dollars\n")
