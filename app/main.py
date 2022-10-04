from app.shops import Shop
from app.customers import Customer


def shop_trip():
    visitors = Customer.open_json_customers()
    for visitor in visitors:
        visitor.print_has_money()
        shops = Shop.open_json_shop()
        price = []
        for shop in shops:
            price.append(visitor.total_product_with_fuel_price(shop))
            print(f"{visitor.name}'s trip to the "
                  f"{shop.name} costs {visitor.total_product_with_fuel_price(shop)}")
        min_price = price.index(min(price))
        if visitor.money < visitor.total_product_with_fuel_price(shops[min_price]):
            return print(f"{visitor.name} "
                         f"doesn't have enough money to make purchase in any shop")
        shop_with_min_price = shops[min_price]
        home = visitor.location
        visitor.print_go_to_shop(shop_with_min_price)

        shop_with_min_price.print_the_bill(visitor)

        visitor.print_go_to_home()
        visitor.location = home
        print(visitor.print_change_balance(shop_with_min_price))



# if __name__ == "__main__":
#     shop_trip()

    # with open("app/config.json") as json_file:
    #     config = json.load(json_file)
    #
    #
    # customers = []
    # shops = []
    # for customer in config["customers"]:
    #     customers.append(
    #         Customer(
    #             customer["name"],
    #             customer["product_cart"],
    #             customer["location"],
    #             customer["money"],
    #             customer["car"]["fuel_consumption"],
    #         )
    #     )
    # for shop in config["shops"]:
    #     shops.append(Shop(shop["name"], shop["location"], shop["products"]))

# def print_has_money(self):
#     for customer in customers:
#         print(f"{customer.name} has {customer.money} dollars")
#
# def distance(shops: list):
#         for
#         x = shop.location[0]


