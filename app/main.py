from app.customers import Customer, Shop, Car
import app.data_file


def shop_trip() -> None:
    # write your code here
    list_customers = [Customer(customer["name"],
                               customer["location"],
                               customer["product_cart"],
                               customer["money"],
                               Car(**customer["car"]))
                      for customer in app.data_file.customers]

    list_shops = [Shop(shop["name"], shop["location"], shop["products"])
                  for shop in app.data_file.shops]

    for customer in list_customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_choose = {}
        for shop in list_shops:
            price = round(customer.all_trip_cost(shop), 2)
            shop_choose[shop.name] = price

            print(f"{customer.name}'s trip to the {shop.name} costs {price}")

        best_shop = customer.choose_better_cost(list_shops)
        if customer.choose_better_cost(list_shops) is not None:
            print(f"{customer.name} rides to {best_shop}\n")

        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            return

        home_location = customer.location
        selected_shop = customer.make_shop(best_shop, list_shops)

        amount = customer.make_check(best_shop, list_shops)
        print(f"Total cost is {amount} dollars\n"
              f"See you again!\n\n{customer.name} rides home")
        customer.location = home_location
        rest = round(customer.money - amount
                     - 2 * customer.cost_trip(selected_shop), 2)
        print(f"{customer.name} now has {rest} dollars\n")


if __name__ == "__main__":
    shop_trip()
