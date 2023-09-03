import datetime


class Shop:

    @staticmethod
    def total_shop_price(name: str, shops_name: str, price: float):
        print(f"{name}'s trip to the {shops_name} costs {price}")

    @staticmethod
    def cheapest_shop(name: str, shops_name: str):
        print(f"{name} rides to {shops_name}")

    @staticmethod
    def bought_products(products: list, name, total_products_price):
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {current_time}")
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")

        for product in products:
            print(f"{product[1]} {product[0]} for {product[2]} dollars")

        print(f"Total cost is {total_products_price} dollars")
        print("See you again!")
        print()
